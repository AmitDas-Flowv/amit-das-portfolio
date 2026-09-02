"""Portfolio content for Amit Das.

All page copy lives here as plain Python data so the Jinja2 templates stay
loop-driven and the site is edited by touching this one file. Strings that
carry inline emphasis (``<b>`` / ``<i>``) are marked with ``markup=True`` and
rendered with the ``| safe`` filter in the template — everything else is
auto-escaped by Jinja.
"""

import re
from pathlib import Path

# --- Site-wide meta -------------------------------------------------------

SITE = {
    "name": "Amit Das",
    "first": "Amit",
    "last": "Das",
    "role": "AI Director & Creative Director",
    "location": "Mumbai, India",
    "current": "AI Director · T-Series — Project Fly",
    "email": "amit.d070@gmail.com",
    "meta_description": (
        "Amit Das — AI Director & Creative Director. Luxury, jewellery and "
        "fashion, grounded in thirteen years of filmmaking, cinematography "
        "and direction."
    ),
    "hero_sub": (
        "Where a thirteen-year foundation in <b>filmmaking, cinematography and "
        "post</b> meets <b>generative AI</b> — building the systems that turn "
        "craft into <b>premium content at scale</b>. A luxury, jewellery and "
        "fashion sensibility, from the first idea to the final cut."
    ),
    "copyright": "Amit Das © 2026",
    "footer_role": "AI Director · Mumbai",
}

# --- Top navigation -------------------------------------------------------

NAV = [
    {"label": "Work", "href": "#work"},
    {"label": "Story", "href": "#story"},
    {"label": "Craft", "href": "#craft"},
    {"label": "Contact", "href": "#contact"},
]

# --- Hero stats -----------------------------------------------------------

STATS = [
    {"value": "13", "suffix": "+", "label": "Years directing image"},
    {"value": "100", "suffix": "+", "label": "Productions & commissions"},
    {"value": "40", "suffix": "+", "label": "Brands & platforms"},
    {"value": "4", "suffix": "", "label": "Published AI films"},
]

# --- Introduction ---------------------------------------------------------

INTRO = {
    "head": "From the camera<br>to the system.",
    "lede": (
        "A filmmaker who learned the frame the long way — now directing the "
        "systems that make content at scale."
    ),
    "body": [
        "Amit Das is a Mumbai-based <b>AI Director and creative director</b> "
        "whose career runs from the edit bay to the production control room to "
        "the generative model.",
        "He began in post and agency video at <b>The Glitch</b> and <b>Concept "
        "Productions</b>, moved into artist and content management at <b>OML</b>, "
        "then spent five-plus years as an independent cinematographer and DOP — "
        "over a hundred branded films, OTT campaigns, episodic shows, music and "
        "fashion films, automotive and travel pieces, and social-first work for "
        "<b>Netflix, Meta, Dell, Mahindra, Lakmé, Gillette, Agoda</b> and many "
        "more.",
        "He traveled to London on the <b>marketing campaign for <i>83</i></b>, "
        "embedded with <b>Mumbai Indians</b> through the IPL, directed two "
        "seasons of the <b>NCPA Symphony Orchestra of India</b> live from a "
        "six-camera PCR, and designed jewellery and product creatives for U.S. "
        "house <b>Mercury Ring</b>.",
        "Today, as <b>AI Director at T-Series</b>, he builds end-to-end — "
        "generation, direction and edit — bringing that production foundation "
        "into AI-led creative direction with a luxury focus.",
        "The real shift is in <b>how</b> he works: thinking in systems rather "
        "than single shots, and pairing deep production and marketing experience "
        "with generative pipelines to <b>design, direct and deliver premium "
        "content at a scale</b> that wasn’t possible before. The craft stays — "
        "the output multiplies. It’s the move from making one film at a time to "
        "<b>leading the system that makes many</b>.",
    ],
}

# --- Work: client-facing verticals (compartments) -------------------------
#
# Each WORK item declares a `primary` vertical (the section it lives in) and a
# list of `tags` (all the facets it belongs to). The filter bar is built from
# CATEGORIES, and a chip cross-filters every section at once — so Amit can open
# (or deep-link) the site to a specific client type. `slug` is the stable id
# used to auto-resolve an uploaded still at static/img/work/<slug>.(jpg|webp|png).

CATEGORIES = [
    {
        "slug": "ai",
        "label": "AI & Generative",
        "blurb": "End-to-end AI films — generation, direction and edit, owned "
        "from first frame to final cut. Built for brands scaling premium "
        "content with generative pipelines.",
    },
    {
        "slug": "fashion",
        "label": "Fashion, Luxury & Jewellery",
        "blurb": "A luxury sensibility across jewellery, fashion and beauty — "
        "studio fashion films, lookbooks and product-led design.",
    },
    {
        "slug": "music",
        "label": "Music & Performance",
        "blurb": "Music videos and visualisers, plus broadcast-grade live "
        "direction — including six-camera orchestral PCR calling.",
    },
    {
        "slug": "brands",
        "label": "Brands & OTT",
        "blurb": "Campaign films and digital commercials for global brands and "
        "streaming platforms — from concept to delivery.",
    },
    {
        "slug": "auto",
        "label": "Automotive & Travel",
        "blurb": "Long-form expedition and road films with a cinematographer’s "
        "eye for landscape, motion and machine.",
    },
    {
        "slug": "food",
        "label": "Food & Hospitality",
        "blurb": "Premium restaurant, product and menu-launch content — appetite "
        "on demand, at social speed.",
    },
    {
        "slug": "live",
        "label": "Live & Sport",
        "blurb": "Embedded, fast-turnaround content and multi-camera direction "
        "for sport, events and film campaigns.",
    },
]

WORK = [
    # ---- AI & Generative (T-Series · Project Fly) ----
    {
        "slug": "dhamal", "primary": "ai", "tags": ["ai", "music"],
        "title": "Dhamal", "role": "AI Director",
        "client": "T-Series · Project Fly", "year": "2026",
        "meta": "End-to-end AI music video — generation, direction and edit, "
        "first frame to final cut.",
        "href": "https://www.youtube.com/watch?v=U6kMnUTqaeQ", "feature": True,
    },
    {
        "slug": "selfmade", "primary": "ai", "tags": ["ai", "music"],
        "title": "Selfmade", "role": "AI Director",
        "client": "T-Series · Project Fly", "year": "2026",
        "meta": "A fully AI-generated music film — directed and cut in-house.",
        "href": "https://youtu.be/ZPQ_FViOwTY", "feature": True,
    },
    {
        "slug": "amrit-kuber", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gathaye — Dhandevta Kuber", "role": "AI Director",
        "client": "T-Series · Project Fly", "year": "2026",
        "meta": "Mythology reimagined through generative image and video pipelines.",
        "href": "https://www.youtube.com/watch?v=OfO3CA9Yq3Y",
    },
    {
        "slug": "amrit-promo", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gathaye — Promo", "role": "AI Director",
        "client": "T-Series · Project Fly", "year": "2026",
        "meta": "Campaign promo cut — pacing, grade and sound built for the feed.",
        "href": "https://youtu.be/aeL9m0AMjeM",
    },

    # ---- Fashion, Luxury & Jewellery ----
    {
        "slug": "nippon-lookbook", "primary": "fashion", "tags": ["fashion"],
        "title": "Nippon Jewellery — Lookbook", "role": "Cinematographer",
        "client": "Abeat Films", "year": "2025",
        "meta": "Jewellery lookbook film — shot on equipment, graded for the house.",
    },
    {
        "slug": "arpita-mehta", "primary": "fashion", "tags": ["fashion"],
        "title": "JM × Arpita Mehta", "role": "Director of Photography · Edit",
        "client": "Arpita Mehta", "year": "2025",
        "meta": "Designer fashion film — shot and cut end to end.",
    },
    {
        "slug": "lakme", "primary": "fashion", "tags": ["fashion"],
        "title": "Lakmé — Fashion Films", "role": "Cinematography",
        "client": "Lakmé Fashion", "year": "2023",
        "meta": "Studio fashion films for the beauty house.",
        "href": "https://www.instagram.com/reel/CqBFvsWDr-g/",
    },
    {
        "slug": "amit-aggarwal", "primary": "fashion", "tags": ["fashion"],
        "title": "Amit Aggarwal — Fashion Film", "role": "Cinematography",
        "client": "Amit Aggarwal", "year": "2023",
        "meta": "Couture fashion film for the Indian designer.",
        "href": "https://www.instagram.com/reel/Cn51GuGgvqS/",
    },
    {
        "slug": "mercury-ring", "primary": "fashion", "tags": ["fashion", "design"],
        "title": "Mercury Ring", "role": "Graphic Designer",
        "client": "Mercury Ring · USA", "year": "2024",
        "meta": "Posters, invitations and jewellery-product creatives for the "
        "U.S. lab-grown diamond house.",
    },

    # ---- Music & Performance ----
    {
        "slug": "bella-ciao", "primary": "music", "tags": ["music", "brands"],
        "title": "Netflix — Money Heist · Bella Ciao",
        "role": "Director of Photography", "client": "Netflix", "year": "2020",
        "meta": "Official India video for the Money Heist campaign.",
        "href": "https://www.youtube.com/watch?v=0TxfLdJ24VM", "feature": True,
    },
    {
        "slug": "boya", "primary": "music", "tags": ["music"],
        "title": "Boya", "role": "Director of Photography", "client": "Boya",
        "year": "",
        "meta": "Music video, shot on location — beach.",
        "href": "https://www.youtube.com/watch?v=3GDfcWQNbIY",
    },
    {
        "slug": "chalta-hai", "primary": "music", "tags": ["music"],
        "title": "Chalta Hai — Shalmali Kholgade",
        "role": "Cinematography", "client": "2XSideB", "year": "",
        "meta": "Music visualiser for the 2XSideB release.",
        "href": "https://youtu.be/qJXqMFABwBE",
    },
    {
        "slug": "yamaha-cfx", "primary": "music", "tags": ["music"],
        "title": "Yamaha Music — CFX", "role": "Director",
        "client": "Yamaha Music · Canopy Media", "year": "2026",
        "meta": "Lead director credit — concert-grand performance film.",
    },
    {
        "slug": "soi", "primary": "music", "tags": ["music", "live"],
        "title": "Symphony Orchestra of India", "role": "Director · PCR, 6-camera",
        "client": "NCPA · SOI", "year": "2025–26",
        "meta": "Directed two seasons of India’s national orchestra live from "
        "a six-camera PCR — calling cuts in real time.",
    },

    # ---- Brands & OTT ----
    {
        "slug": "meta", "primary": "brands", "tags": ["brands"],
        "title": "Meta — Campaign", "role": "Cinematography", "client": "Meta",
        "year": "",
        "meta": "Campaign film — digital commercial.",
        "href": "https://youtu.be/Nf8H6MNKMYE",
    },
    {
        "slug": "buzzfeed", "primary": "brands", "tags": ["brands"],
        "title": "BuzzFeed India", "role": "Director of Photography",
        "client": "BuzzFeed India", "year": "",
        "meta": "<i>If Opinions Were Sold Like Clothes</i> — shot on location.",
        "href": "https://youtu.be/8sdRN6aMmwM",
    },
    {
        "slug": "netflix-royals", "primary": "brands", "tags": ["brands"],
        "title": "Netflix — The Royals", "role": "Cinematography · Edit",
        "client": "Netflix · Canopy Media", "year": "2025",
        "meta": "Cinematography and edit for the Netflix title campaign.",
    },
    {
        "slug": "dell-futurist", "primary": "brands", "tags": ["brands"],
        "title": "Dell — Futurist", "role": "Cinematography", "client": "Dell",
        "year": "",
        "meta": "On-location sound-studio commercial.",
        "href": "https://www.youtube.com/watch?v=0aA_OYV4GAI",
    },
    {
        "slug": "godaddy", "primary": "brands", "tags": ["brands"],
        "title": "GoDaddy", "role": "Cinematography", "client": "GoDaddy",
        "year": "",
        "meta": "Green-screen digital commercial.",
        "href": "https://youtu.be/mNY8RD2xAxo",
    },
    {
        "slug": "netflix-govt", "primary": "brands", "tags": ["brands"],
        "title": "Netflix × Govt. of India", "role": "Director of Photography",
        "client": "Netflix", "year": "",
        "meta": "Outdoor campaign film from a seven-film series.",
        "href": "https://youtu.be/kBD2Dfr4rek",
    },
    {
        "slug": "zingbus", "primary": "brands", "tags": ["brands"],
        "title": "Zingbus — TVC", "role": "Cinematography", "client": "Zingbus",
        "year": "",
        "meta": "Studio TVC.",
        "href": "https://youtu.be/b8k1QdpL2SQ",
    },
    {
        "slug": "groww", "primary": "brands", "tags": ["brands"],
        "title": "Groww — Digital Studio", "role": "Cinematography",
        "client": "Groww", "year": "",
        "meta": "Digital studio-setup films.",
        "href": "https://www.youtube.com/watch?v=T8X84rLyXss",
    },

    # ---- Automotive & Travel ----
    {
        "slug": "mahindra-mojo", "primary": "auto", "tags": ["auto"],
        "title": "Mahindra Mojo — The Mountain Trail",
        "role": "Director of Photography", "client": "Mahindra", "year": "",
        "meta": "Chandigarh to Leh — a long-form expedition film.",
        "href": "https://www.youtube.com/watch?v=HVCBrHU4ANQ", "feature": True,
    },
    {
        "slug": "mg-motoroctane", "primary": "auto", "tags": ["auto"],
        "title": "MG × MotorOctane", "role": "Director of Photography",
        "client": "MG", "year": "",
        "meta": "Mumbai to Delhi road film.",
        "href": "https://www.youtube.com/watch?v=vv6BsobrThk",
    },
    {
        "slug": "agoda", "primary": "auto", "tags": ["auto"],
        "title": "Agoda — Travel", "role": "Videographer", "client": "Agoda",
        "year": "",
        "meta": "Travel reels shot on location.",
        "href": "https://www.instagram.com/reel/CkLtqonA7vq/",
    },

    # ---- Food & Hospitality ----
    {
        "slug": "akina", "primary": "food", "tags": ["food"],
        "title": "Akina — Bandra", "role": "Cinematography",
        "client": "Akina", "year": "",
        "meta": "Social-first food content for the premium Japanese flagship.",
        "href": "https://www.instagram.com/reel/Co7Y_pZoDUH/",
    },
    {
        "slug": "faasos", "primary": "food", "tags": ["food"],
        "title": "Faasos — Pizza Wraps Launch", "role": "Production · Food Films",
        "client": "Rebel Foods", "year": "2025",
        "meta": "New-product launch films for the QSR brand.",
    },
    {
        "slug": "oven-story", "primary": "food", "tags": ["food"],
        "title": "Oven Story", "role": "Videography · Photography",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Menu and product marketing content.",
    },
    {
        "slug": "eu-food-show", "primary": "food", "tags": ["food"],
        "title": "European Union — Food Show", "role": "Cinematography",
        "client": "European Union", "year": "",
        "meta": "Food show and recipe films.",
        "href": "https://www.instagram.com/tv/CgJZqERq7by/",
    },

    # ---- Live & Sport ----
    {
        "slug": "mumbai-indians", "primary": "live", "tags": ["live"],
        "title": "Mumbai Indians — IPL",
        "role": "Content Producer · Cinematographer",
        "client": "Mumbai Indians", "year": "2023",
        "meta": "Travelled with the team through the May 2023 season — "
        "fast-turnaround social and campaign content.",
    },
    {
        "slug": "film-83", "primary": "live", "tags": ["live"],
        "title": "83 — Film Marketing", "role": "Social Media Videographer",
        "client": "Reliance Media · London", "year": "2019",
        "meta": "Three-month campaign contract on the <i>83</i> release, on "
        "location in London.",
    },
    {
        "slug": "booyah", "primary": "live", "tags": ["live"],
        "title": "Garena — Booyah Awards", "role": "Camera Operator",
        "client": "OML Studios · Garena", "year": "2026",
        "meta": "Live esports awards multi-camera coverage.",
    },
    {
        "slug": "football", "primary": "live", "tags": ["live"],
        "title": "Football", "role": "Cinematography", "client": "FS Media Pro",
        "year": "2025",
        "meta": "On-ground sports film.",
    },
]

# --- Career timeline (Section 00:04) --------------------------------------

TIMELINE = [
    {
        "year": "2026 —",
        "title": "AI Director",
        "org": "T-Series · Project Fly",
        "body": "Contract, full-time. End-to-end AI-video production across "
        "music video and mythology.",
        "now": True,
    },
    {
        "year": "2025 – 26",
        "title": "Founder / Director",
        "org": "FLOWV",
        "body": "Independent creative studio — direction, cinematography, edit "
        "and production. Rebel Foods culinary launches, Yamaha Music, NCPA SOI.",
        "now": False,
    },
    {
        "year": "2024",
        "title": "Graphic Designer",
        "org": "Mercury Ring · USA",
        "body": "Remote, full-time. Jewellery product and marketing creatives.",
        "now": False,
    },
    {
        "year": "2018 – 23",
        "title": "Cinematographer & DOP",
        "org": "Independent",
        "body": "100+ commissions — OTT, branded film, fashion, automotive, "
        "travel, food and live. Netflix, Meta, Dell, Lakmé, Mahindra, Flipkart, "
        "Agoda and more.",
        "now": False,
    },
    {
        "year": "2017 – 18",
        "title": "Content Manager",
        "org": "Only Much Louder (OML)",
        "body": "Artist content and sponsor deals — Zakir Khan, Nishant Tanwar, "
        "Gaurav Kapoor.",
        "now": False,
    },
    {
        "year": "2013 – 17",
        "title": "Editor · DOP · Producer",
        "org": "The Glitch → Concept Productions",
        "body": "Post-production and end-to-end video workflow across agency "
        "and production.",
        "now": False,
    },
]

# --- Craft / capabilities (Section 00:05) ---------------------------------

CAPABILITIES = [
    {
        "title": "Direction & Craft",
        "entries": [
            "AI-led creative direction",
            "Content systems & production at scale",
            "Cinematography & visual language",
            "Editing & post-production",
            "Producing & client delivery",
            "Creative & team leadership",
        ],
    },
    {
        "title": "Generative AI Stack",
        "entries": [
            "Kling · Veo · Seedance · Runway",
            "Higgsfield · Pika · Nano Banana",
            "Google AI Studio · Vertex AI",
            "ComfyUI · LoRA workflows",
            "LLMs & multimodal pipelines",
            "Agentic & app-building tools",
        ],
    },
    {
        "title": "Formats & Sectors",
        "entries": [
            "Luxury, jewellery & fashion film",
            "Music video & visualiser",
            "OTT & branded campaigns",
            "Food, product & hospitality",
            "Automotive & travel",
            "Live performance & sport",
        ],
    },
]

# --- Client marquee -------------------------------------------------------

CLIENTS = [
    "T-Series", "Netflix", "Mumbai Indians", "Meta", "Dell", "Lakmé",
    "Mahindra", "Amazon miniTV", "Gillette", "Agoda", "Spotify", "Flipkart",
    "NCPA", "Rebel Foods", "Yamaha", "GoDaddy", "Volkswagen", "Citi", "Uber",
    "MTV",
]

# --- Contact socials ------------------------------------------------------

SOCIALS = [
    {"label": "Instagram", "href": "https://instagram.com/amitda5"},
    {"label": "Portfolio", "href": "https://amitdasvideography.myportfolio.com/"},
    {
        "label": "Behance",
        "href": "https://www.behance.net/collection/176241147/Homemade-Series",
    },
    {"label": "Vimeo", "href": "https://vimeo.com/showcase/3366175"},
]

CONTACT = {
    "cue": "End Card · Let’s Make Something",
    "big": "Available to lead AI direction, creative direction, and content "
    "built at scale.",
}


# --- Hero reel / montage --------------------------------------------------
# Drop in a real sizzle reel later by setting one of these; while all are None
# the hero plays a silent auto-montage of the work stills instead.
REEL = {
    "youtube_id": None,   # e.g. "U6kMnUTqaeQ" for a muted looping hero reel
    "vimeo_id": None,
    "mp4": None,          # e.g. "video/reel.mp4" under static/
}


# --- Thumbnail + work helpers ---------------------------------------------

_WORK_IMG_DIR = Path(__file__).resolve().parent / "static" / "img" / "work"
_YT_RE = re.compile(r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|v/))([\w-]{11})")


def youtube_id(href):
    """Extract an 11-char YouTube id from watch/youtu.be/embed URLs."""
    if not href:
        return None
    m = _YT_RE.search(href)
    return m.group(1) if m else None


def _uploaded_still(slug):
    """Return a static-relative path if a still was dropped at
    static/img/work/<slug>.<ext>, else None."""
    if not slug:
        return None
    for ext in ("jpg", "jpeg", "webp", "png"):
        if (_WORK_IMG_DIR / f"{slug}.{ext}").exists():
            return f"img/work/{slug}.{ext}"
    return None


def _resolve_thumb(item):
    """(src, is_external). Priority: explicit thumb → uploaded still by slug →
    YouTube auto-thumbnail → None (graded-gradient fallback)."""
    if item.get("thumb"):
        return item["thumb"], False
    still = _uploaded_still(item.get("slug", ""))
    if still:
        return still, False
    yid = youtube_id(item.get("href"))
    if yid:
        return f"https://img.youtube.com/vi/{yid}/maxresdefault.jpg", True
    return None, False


def _cta(href):
    if not href:
        return None
    if "instagram.com" in href:
        return "View on Instagram"
    if "youtu" in href or "facebook.com" in href:
        return "Watch"
    return "View"


def _decorate(item):
    src, external = _resolve_thumb(item)
    return {
        **item,
        "thumb_src": src,
        "thumb_external": external,
        "yt_id": youtube_id(item.get("href")),
        "cta": _cta(item.get("href")),
        "tagstr": " ".join(item.get("tags", [])),
    }


def work_by_category():
    """Return (groups, decorated). `groups` = each non-empty CATEGORY with its
    decorated items; `decorated` = every item, flat."""
    decorated = [_decorate(w) for w in WORK]
    groups = []
    for cat in CATEGORIES:
        items = [w for w in decorated if w["primary"] == cat["slug"]]
        if items:
            groups.append({**cat, "pieces": items})
    return groups, decorated


def montage_frames(decorated):
    """De-duplicated still URLs for the hero montage (only items that resolve
    to a real image — YouTube auto-thumbs or uploaded stills)."""
    seen, frames = set(), []
    for w in decorated:
        src = w["thumb_src"]
        if src and src not in seen:
            seen.add(src)
            frames.append(src)
    return frames


def as_context():
    """Return every content block as a single dict for ``render_template``."""
    groups, decorated = work_by_category()
    return {
        "SITE": SITE,
        "NAV": NAV,
        "STATS": STATS,
        "INTRO": INTRO,
        "CATEGORIES": CATEGORIES,
        "WORK_GROUPS": groups,
        "MONTAGE": montage_frames(decorated),
        "REEL": REEL,
        "TIMELINE": TIMELINE,
        "CAPABILITIES": CAPABILITIES,
        "CLIENTS": CLIENTS,
        "SOCIALS": SOCIALS,
        "CONTACT": CONTACT,
    }
