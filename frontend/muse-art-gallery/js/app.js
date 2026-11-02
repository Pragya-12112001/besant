document.addEventListener("DOMContentLoaded", () => {
  const grid = document.querySelector("#gallery-grid");
  const searchForm = document.querySelector("#search-form");
  const searchInput = document.querySelector("#search-input");
  const loadMoreButton = document.querySelector("#load-more");
  const emptyState = document.querySelector("#empty-state");
  const resultsCount = document.querySelector("#results-count");
  const filterButtons = [...document.querySelectorAll(".filter-chip")];
  const menuToggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".desktop-nav");

  let currentQuery = "painting";
  let currentOffset = 0;
  let isLoading = false;
  let hasMore = true;
  let visibleCount = 0;
  let seenIds = new Set();

  function showStatus(message) {
    const status = document.querySelector("#status-message");
    if (!status) return;
    status.textContent = message;
    status.classList.add("visible");
    window.setTimeout(() => status.classList.remove("visible"), 2800);
  }

  function renderCard(artwork) {
    const card = document.createElement("article");
    card.className = "art-card";

    const link = document.createElement("a");
    link.className = "art-card-link";
    link.href = `artwork.html?id=${encodeURIComponent(artwork.objectID)}`;
    link.setAttribute("aria-label", `View ${cleanText(artwork.title, "artwork")}`);

    const imageWrap = document.createElement("div");
    imageWrap.className = "art-card-image";

    const image = document.createElement("img");
    image.src = getArtworkImage(artwork);
    image.alt = `${cleanText(artwork.title, "Artwork")} by ${cleanText(artwork.artistDisplayName, "unknown artist")}`;
    image.loading = "lazy";
    image.decoding = "async";

    const index = document.createElement("span");
    index.className = "art-card-index";
    index.textContent = String(visibleCount + 1).padStart(2, "0");

    const arrow = document.createElement("span");
    arrow.className = "art-card-arrow";
    arrow.textContent = "↗";

    imageWrap.append(image, index, arrow);

    const info = document.createElement("div");
    info.className = "art-card-info";

    const textGroup = document.createElement("div");
    const title = document.createElement("h3");
    title.textContent = cleanText(artwork.title, "Untitled");
    const artist = document.createElement("p");
    artist.textContent = cleanText(artwork.artistDisplayName, "Artist unknown");
    textGroup.append(title, artist);

    const year = document.createElement("p");
    year.className = "art-card-year";
    year.textContent = cleanText(artwork.objectDate, "");

    info.append(textGroup, year);
    link.append(imageWrap, info);
    card.append(link);
    return card;
  }

  function renderArtworks(artworks, append = false) {
    if (!append) grid.innerHTML = "";
    const fragment = document.createDocumentFragment();

    artworks.forEach((artwork) => {
      const id = String(artwork.objectID);
      if (seenIds.has(id)) return;
      seenIds.add(id);
      visibleCount += 1;
      fragment.append(renderCard(artwork));
    });

    grid.append(fragment);
    resultsCount.textContent = `${visibleCount} WORKS`;
    emptyState.hidden = visibleCount !== 0;
  }

  async function loadArtworks({ reset = false } = {}) {
    if (isLoading || (!hasMore && !reset)) return;
    isLoading = true;
    loadMoreButton.hidden = true;

    if (reset) {
      currentOffset = 0;
      visibleCount = 0;
      seenIds = new Set();
      grid.innerHTML = '<div class="loading-state"><span class="loader"></span><p>Gathering something beautiful...</p></div>';
      resultsCount.textContent = "DISCOVERING";
      emptyState.hidden = true;
      hasMore = true;
    }

    try {
      const result = await getPublicArtworks(currentQuery, currentOffset, 24);
      if (reset) grid.innerHTML = "";
      renderArtworks(result.artworks, true);
      currentOffset = result.nextOffset;
      hasMore = result.received > 0 && currentOffset < 10000;
      loadMoreButton.hidden = !hasMore;
      if (visibleCount === 0) {
        emptyState.hidden = false;
        emptyState.textContent = hasMore
          ? "No public-domain images in this batch. Load more to keep exploring."
          : "No artworks found for that search. Try another artist or subject.";
      }
      if (result.artworks.length === 0 && result.received > 0 && hasMore) {
        showStatus("Looking for more public-domain images...");
      }
    } catch (error) {
      console.error(error);
      if (visibleCount === 0) {
        grid.innerHTML = "";
        emptyState.hidden = false;
        emptyState.textContent = "The collection could not load right now. Please check your connection and try again.";
      } else {
        showStatus("Could not load more artworks. Please try again.");
      }
    } finally {
      isLoading = false;
    }
  }

  function chooseQuery(query, button) {
    currentQuery = query;
    filterButtons.forEach((chip) => chip.classList.toggle("active", chip === button));
    searchInput.value = "";
    loadArtworks({ reset: true });
  }

  searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = searchInput.value.trim();
    if (!query) {
      showStatus("Enter an artist, artwork or subject to search.");
      return;
    }
    currentQuery = query;
    filterButtons.forEach((chip) => chip.classList.remove("active"));
    loadArtworks({ reset: true });
  });

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => chooseQuery(button.dataset.query, button));
  });

  loadMoreButton.addEventListener("click", () => loadArtworks());

  if (menuToggle) {
    menuToggle.addEventListener("click", () => {
      const isOpen = nav.classList.toggle("open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
      menuToggle.textContent = isOpen ? "×" : "☰";
    });
    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        nav.classList.remove("open");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.textContent = "☰";
      });
    });
  }

  // Featured artwork uses the example object ID supplied during project planning.
  getArtwork("436535").then((artwork) => {
    if (!hasUsablePublicImage(artwork)) return;
    document.querySelector("#hero-image").src = getArtworkImage(artwork);
    document.querySelector("#hero-image").alt = `${artwork.title} by ${artwork.artistDisplayName}`;
    document.querySelector("#hero-title").textContent = cleanText(artwork.title);
    document.querySelector("#hero-artist").textContent =
      `${cleanText(artwork.artistDisplayName)} · ${cleanText(artwork.objectDate)}`;
    document.querySelector("#hero-link").href = `artwork.html?id=${artwork.objectID}`;
  }).catch((error) => console.warn("Featured artwork could not be loaded:", error));

  loadArtworks({ reset: true });
});
