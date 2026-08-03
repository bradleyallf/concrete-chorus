# The Concrete Chorus Project website

This repository contains the public website for The Concrete Chorus Project, a Colorado State University community-science study of urban bird diversity. The site is published at [www.concretechorus.org](https://www.concretechorus.org/) using GitHub Pages.

## How the site works

The website is intentionally framework-free. GitHub Pages serves the HTML, CSS, JavaScript, images, and self-contained interactive maps directly from the `main` branch.

- `index.html` is the home page.
- `background.html`, `instructions.html`, and `questions.html` contain the main project information.
- `participating_cities_*.html` contains one page for each participating city.
- `*_map.html` and `*_sample.html` files are exported interactive maps embedded in city pages with iframes.
- `styles.css` contains shared site styling.
- `site.js` controls the participating-cities menu.
- `data/` contains media retained for project results and future site development. It is not currently linked from the public pages.
- `archive/2025/` contains superseded 2025 material retained for reference.
- `archive/planned-cities/` contains city pages and maps that were prepared but not used for data collection. These can be restored if a city participates in a future season.

The `CNAME` file connects GitHub Pages to the custom domain and should not be removed or renamed.

## Making routine updates

Edit the relevant HTML file directly. Use relative links so pages continue to work both locally and on GitHub Pages.

When adding a city:

1. Copy an existing `participating_cities_*.html` page and update its title, heading, text, iframe source, and iframe title.
2. Add the city link to the participating-cities menu on each public page. The header markup is repeated because this site does not use a build system or server-side includes.
3. Add the exported map file at the repository root unless the existing page structure is deliberately reorganized.
4. Run the link checker described below.

Global visual changes should usually be made in `styles.css`, not repeated in individual pages. Page-specific layout can remain inline when it is used only once.

## Checking changes locally

Start a small local web server from the repository root:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000/`. Using a local server is preferable to opening HTML files directly because it more closely matches GitHub Pages and supports embedded map behavior.

Check internal links and referenced files with:

```sh
python3 scripts/check_links.py
```

Before publishing, review the home page, navigation, instructions, questions, and every city page on both a desktop-width and phone-width screen. Confirm that interactive maps load and that seasonal dates and recruitment language are current.

## Publishing

Changes merged or pushed to the configured GitHub Pages publishing branch are deployed by GitHub. This repository currently uses `main`. Allow a few minutes for the public site and custom-domain cache to update.

## Archiving old material

Move superseded pages and assets into a clearly labeled folder under `archive/` rather than deleting potentially useful project history. Archived pages are not linked in the public navigation. Moving a published file changes its old direct URL, so verify that no current page references it first.

## Large media files

This repository includes large WAV and image files. Avoid adding duplicate exports or raw files that will not be used by the website. Git retains earlier versions even after a file is moved or deleted, so large-file cleanup should be planned separately rather than handled as routine housekeeping.
