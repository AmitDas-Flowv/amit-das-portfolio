# Work thumbnails

Drop a still here named after a piece's **slug** and it appears on that card
automatically — no code change. Format: `.jpg`/`.jpeg`/`.webp`/`.png` (checked in
that order), 16:9, ~1280–1600px wide (`object-fit: cover`). The slug is the
`"slug"` value in `content.py`.

## Current state

- **16 YouTube-linked pieces** pull their still automatically — no file needed.
- **17 pieces** now ship an **AI-generated placeholder still** (Magnific,
  cinematic 16:9). These are stand-ins — replace any of them with a real frame
  from the actual production by overwriting the same filename:

  `mercury-ring, nippon-lookbook, arpita-mehta, lakme, amit-aggarwal,
  yamaha-cfx, soi, netflix-royals, agoda, akina, faasos, oven-story,
  eu-food-show, mumbai-indians, film-83, booyah, football`

Example: drop a real `mercury-ring.jpg` here and it replaces the placeholder.
