/* MUSE API layer — all requests to The Met live here. */
const MET_API = "https://collectionapi.metmuseum.org/public/collection";

const objectCache = new Map();

async function requestJSON(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`The collection service responded with ${response.status}.`);
  }
  return response.json();
}

async function searchArtworkIds(query, offset = 0, limit = 30) {
  const params = new URLSearchParams({
    q: query,
    hasImages: "true",
    limit: String(limit),
    offset: String(offset)
  });

  // Search uses v1.1; object records remain on v1.
  return requestJSON(`${MET_API}/v1.1/search?${params.toString()}`);
}

async function getArtwork(objectId) {
  const id = String(objectId);
  if (objectCache.has(id)) return objectCache.get(id);

  const artwork = await requestJSON(`${MET_API}/v1/objects/${encodeURIComponent(id)}`);
  objectCache.set(id, artwork);
  return artwork;
}

function hasUsablePublicImage(artwork) {
  return Boolean(
    artwork &&
    artwork.isPublicDomain === true &&
    (artwork.primaryImageSmall || artwork.primaryImage)
  );
}

function getArtworkImage(artwork) {
  return artwork.primaryImageSmall || artwork.primaryImage || "";
}

function cleanText(value, fallback = "Not listed") {
  if (value === null || value === undefined || String(value).trim() === "") return fallback;
  return String(value).trim();
}

async function getPublicArtworks(query, offset = 0, limit = 24) {
  const search = await searchArtworkIds(query, offset, limit);
  const ids = Array.isArray(search.objectIDs) ? search.objectIDs : [];

  // Fetch a modest batch in parallel, then only show records with public-domain images.
  const records = new Array(ids.length);
  let nextIndex = 0;

  // Keep the request burst modest; the public API can throttle aggressive clients.
  async function worker() {
    while (nextIndex < ids.length) {
      const index = nextIndex++;
      try {
        records[index] = await getArtwork(ids[index]);
      } catch (error) {
        console.warn(`Could not load artwork ${ids[index]}:`, error);
        records[index] = null;
      }
    }
  }

  const workerCount = Math.min(5, ids.length);
  await Promise.all(Array.from({ length: workerCount }, () => worker()));

  return {
    artworks: records.filter(hasUsablePublicImage),
    total: search.total || 0,
    received: ids.length,
    nextOffset: offset + ids.length
  };
}
