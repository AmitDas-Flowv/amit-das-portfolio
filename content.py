"""Portfolio content for Amit Das.

All page copy lives here as plain Python data so the Jinja2 templates stay
loop-driven and the site is edited by touching this one file. Strings that
carry inline emphasis (``<b>`` / ``<i>``) are marked with ``markup=True`` and
rendered with the ``| safe`` filter in the template — everything else is
auto-escaped by Jinja.
"""

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

# --- Published AI films (Section 00:02) -----------------------------------

AI_FILMS = [
    {
        "frameno": "01",
        "tag": "Music Video · AI",
        "title": "Dhamal",
        "meta": (
            "End-to-end AI music video — generation, direction and edit, from "
            "first frame to final cut."
        ),
        "href": "https://www.youtube.com/watch?v=U6kMnUTqaeQ",
        "cta": "Watch on YouTube",
        "feature": True,
    },
    {
        "frameno": "02",
        "tag": "Music Video · AI",
        "title": "Selfmade",
        "meta": "A fully AI-generated music film — directed and cut in-house.",
        "href": "https://youtu.be/ZPQ_FViOwTY",
        "cta": "Watch on YouTube",
        "feature": True,
    },
    {
        "frameno": "03",
        "tag": "AI Mythology",
        "title": "Amrit Gathaye<br>Dhandevta Kuber",
        "meta": "Mythology reimagined through generative image and video pipelines.",
        "href": "https://www.youtube.com/watch?v=OfO3CA9Yq3Y",
        "cta": "Watch",
        "feature": False,
    },
    {
        "frameno": "04",
        "tag": "AI Mythology · Promo",
        "title": "Amrit Gathaye<br>Promo",
        "meta": "Campaign promo cut — pacing, grade and sound built for the feed.",
        "href": "https://youtu.be/aeL9m0AMjeM",
        "cta": "Watch",
        "feature": False,
    },
]

# --- Selected cinematography & direction (Section 00:03) ------------------

CINEMA_WORK = [
    {
        "role": "Director of Photography",
        "title": "Netflix — Money Heist<br>"
        "<span class='italic text-gold-lift'>Bella Ciao</span>",
        "meta": "Official India video for the Money Heist campaign.",
        "href": "https://www.youtube.com/watch?v=0TxfLdJ24VM",
    },
    {
        "role": "DOP · Travel Film",
        "title": "Mahindra Mojo<br>The Mountain Trail",
        "meta": "Chandigarh to Leh — a long-form expedition film.",
        "href": "https://www.youtube.com/watch?v=HVCBrHU4ANQ",
    },
    {
        "role": "Director of Photography",
        "title": "BuzzFeed India",
        "meta": "<i>If Opinions Were Sold Like Clothes</i> — shot on location.",
        "href": "https://youtu.be/8sdRN6aMmwM",
    },
    {
        "role": "Cinematography",
        "title": "Meta",
        "meta": "Campaign film — digital commercial.",
        "href": "https://youtu.be/Nf8H6MNKMYE",
    },
    {
        "role": "DOP · Travel Film",
        "title": "MG × MotorOctane",
        "meta": "Mumbai to Delhi road film.",
        "href": "https://www.youtube.com/watch?v=vv6BsobrThk",
    },
    {
        "role": "Director of Photography",
        "title": "Boya",
        "meta": "Music video, shot on location — beach.",
        "href": "https://www.youtube.com/watch?v=3GDfcWQNbIY",
    },
]

# --- Signature credits without a public link (Section 00:03) --------------

SIGNATURE = [
    {
        "tag": "2023 · Sports",
        "title": "Mumbai Indians — IPL",
        "body": "Content Producer & Cinematographer, traveling with the team "
        "through the May 2023 season.",
    },
    {
        "tag": "2019 · Film Marketing",
        "title": "83 — Reliance Media",
        "body": "Social Media Videographer on the <i>83</i> campaign; a "
        "three-month contract, on location in London.",
    },
    {
        "tag": "2025 – 2026 · Live",
        "title": "Symphony Orchestra of India",
        "body": "Director & live-cut lead across two NCPA seasons for India’s "
        "national orchestra.",
    },
    {
        "tag": "2024 · Design",
        "title": "Mercury Ring",
        "body": "Graphic designer for the U.S. jewellery house — posters, "
        "invitations and product creatives.",
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


def as_context():
    """Return every content block as a single dict for ``render_template``."""
    return {
        "SITE": SITE,
        "NAV": NAV,
        "STATS": STATS,
        "INTRO": INTRO,
        "AI_FILMS": AI_FILMS,
        "CINEMA_WORK": CINEMA_WORK,
        "SIGNATURE": SIGNATURE,
        "TIMELINE": TIMELINE,
        "CAPABILITIES": CAPABILITIES,
        "CLIENTS": CLIENTS,
        "SOCIALS": SOCIALS,
        "CONTACT": CONTACT,
    }
