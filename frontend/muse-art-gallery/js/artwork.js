document.addEventListener("DOMContentLoaded", async () => {
  const params = new URLSearchParams(window.location.search);
  const objectId = params.get("id");
  const loading = document.querySelector("#detail-loading");
  const errorPanel = document.querySelector("#detail-error");
  const article = document.querySelector("#artwork-detail");

  function setText(selector, value, fallback = "Not listed") {
    const element = document.querySelector(selector);
    if (element) element.textContent = cleanText(value, fallback);
  }

  if (!objectId || !/^\d+$/.test(objectId)) {
    loading.hidden = true;
    errorPanel.hidden = false;
    return;
  }

  try {
    const artwork = await getArtwork(objectId);
    if (!artwork || !hasUsablePublicImage(artwork)) {
      throw new Error("This artwork does not have an available public-domain image.");
    }

    document.title = `${cleanText(artwork.title, "Artwork")} — MUSE`;
    setText("#detail-title", artwork.title, "Untitled");
    setText("#detail-artist", artwork.artistDisplayName, "Artist unknown");
    setText("#detail-department", artwork.department, "COLLECTION");
    setText("#detail-number", `OBJECT NO. ${artwork.objectID}`, "");
    setText("#detail-date", artwork.objectDate);
    setText("#detail-medium", artwork.medium);
    setText("#detail-dimensions", artwork.dimensions);
    setText("#detail-department-full", artwork.department);
    setText("#detail-origin", [artwork.country, artwork.culture].filter(Boolean).join(" · "));

    const description = artwork.creditLine
      ? `${cleanText(artwork.artistDisplayName, "The artist")} — ${cleanText(artwork.medium, "medium not listed")}. ${artwork.creditLine}.`
      : `${cleanText(artwork.title, "This work")} is part of The Metropolitan Museum of Art's collection. Explore its details and related subjects below.`;
    setText("#detail-description", description);

    const image = document.querySelector("#detail-image");
    image.src = getArtworkImage(artwork);
    image.alt = `${cleanText(artwork.title)} by ${cleanText(artwork.artistDisplayName, "unknown artist")}`;

    const museumLink = document.querySelector("#museum-link");
    museumLink.href = artwork.objectURL || `https://www.metmuseum.org/art/collection/search/${artwork.objectID}`;

    const tags = document.querySelector("#detail-tags");
    tags.innerHTML = "";
    (artwork.tags || []).slice(0, 8).forEach((tag) => {
      const chip = document.createElement("span");
      chip.textContent = tag.term;
      tags.append(chip);
    });

    loading.hidden = true;
    article.hidden = false;
  } catch (error) {
    console.error(error);
    loading.hidden = true;
    errorPanel.hidden = false;
  }
});
