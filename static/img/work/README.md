# Work thumbnails

Drop a still here and it appears on that piece's card automatically — no code
change needed. The file just has to be named after the piece's **slug**.

- **Format:** `.jpg`, `.jpeg`, `.webp`, or `.png` (checked in that order)
- **Aspect / size:** 16:9, ~1280×720 (larger is fine; it's `object-fit: cover`)
- **Name:** `<slug>.jpg` — the slug is the `"slug"` value in `content.py`.

YouTube-linked pieces already pull their still automatically, so you only need
to add files for the non-YouTube pieces. Slugs that currently have no image:

| Slug | Piece |
|------|-------|
| `nippon-lookbook` | Nippon Jewellery — Lookbook |
| `arpita-mehta` | JM × Arpita Mehta |
| `lakme` | Lakmé — Fashion Films (Instagram) |
| `amit-aggarwal` | Amit Aggarwal — Fashion Film (Instagram) |
| `mercury-ring` | Mercury Ring |
| `yamaha-cfx` | Yamaha Music — CFX |
| `soi` | Symphony Orchestra of India |
| `netflix-royals` | Netflix — The Royals |
| `agoda` | Agoda — Travel (Instagram) |
| `akina` | Akina — Bandra (Instagram) |
| `faasos` | Faasos — Pizza Wraps Launch |
| `oven-story` | Oven Story |
| `eu-food-show` | European Union — Food Show (Instagram) |
| `mumbai-indians` | Mumbai Indians — IPL |
| `film-83` | 83 — Film Marketing |
| `booyah` | Garena — Booyah Awards |
| `football` | Football |

Example: add `mercury-ring.jpg` to this folder and the Mercury Ring card shows it.
