# MUSE — Digital Art Gallery

A responsive art discovery website built with HTML, CSS and vanilla JavaScript using The Metropolitan Museum of Art Collection API.

## Run locally

Because the project uses JavaScript modules? No — it uses regular deferred scripts — but the browser may restrict some local requests depending on your setup. Run it through a local development server for the most reliable experience.

### Option 1: VS Code Live Server
1. Open this folder in VS Code.
2. Install the **Live Server** extension if you do not already have it.
3. Right-click `index.html`.
4. Choose **Open with Live Server**.

### Option 2: Python local server
From this project folder, run:

```bash
python -m http.server 5500
```

Then open `http://localhost:5500`.

## API endpoints

- Search: `https://collectionapi.metmuseum.org/public/collection/v1.1/search`
- Object details: `https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}`

The Met's API search returns object IDs. The app fetches individual object records and displays only works marked `isPublicDomain: true` that have an image URL.

## Project files

- `index.html` — gallery homepage
- `artwork.html` — separate artwork details page
- `css/style.css` — shared design system and homepage styles
- `css/artwork.css` — artwork detail page styles
- `js/api.js` — API requests and shared helpers
- `js/app.js` — homepage search, filters and gallery rendering
- `js/artwork.js` — artwork detail page rendering

## Notes

- Internet access is required for the museum API, artwork images and Google Fonts.
- The Met API is a public service and may occasionally be unavailable or rate-limited.
- Public-domain image availability is checked per artwork record; a search result with an image is not automatically assumed to be public domain.
- Artwork metadata and images are provided by The Metropolitan Museum of Art.
