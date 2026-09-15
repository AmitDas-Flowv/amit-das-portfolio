"""Portfolio content for Amit Das.

All page copy lives here as plain Python data so the Jinja2 templates stay
loop-driven and the site is edited by touching this one file. Strings that
carry inline emphasis (``<b>`` / ``<i>``) are marked with ``markup=True`` and
rendered with the ``| safe`` filter in the template - everything else is
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
    "current": "AI Director · T-Series",
    "email": "amit.d070@gmail.com",
    "archive_url": "https://amitdasvideography.myportfolio.com/",
    "meta_description": (
        "Amit Das, AI Director and Creative Director. Luxury, jewellery and "
        "fashion work, built on thirteen years of filmmaking, cinematography "
        "and direction."
    ),
    "hero_sub": (
        "Thirteen years in <b>filmmaking, cinematography and "
        "post</b>, now building with <b>generative AI</b>. High-end content, and "
        "the systems that produce it, with a luxury, jewellery and "
        "fashion eye."
    ),
    "copyright": "Amit Das © 2026",
    "footer_role": "AI Director · Mumbai",
}

# --- Top navigation -------------------------------------------------------

NAV = [
    {"label": "Work", "href": "/#work"},
    {"label": "Story", "href": "/#story"},
    {"label": "Craft", "href": "/#craft"},
    {"label": "Contact", "href": "#contact"},
]

# --- Hero stats -----------------------------------------------------------

STATS = [
    {"value": "13", "suffix": "+", "label": "Years directing image"},
    {"value": "100", "suffix": "+", "label": "Productions & commissions"},
    {"value": "40", "suffix": "+", "label": "Brands & platforms"},
    {"value": "7", "suffix": "", "label": "Published AI films"},
]

# --- Introduction ---------------------------------------------------------

INTRO = {
    "head": "From the camera<br>to the system.",
    "lede": (
        "A filmmaker who learned the craft the long way, now directing the "
        "systems that make the work, not just the shots."
    ),
    "body": [
        "Amit Das is a Mumbai-based <b>AI Director and creative director</b> "
        "whose career runs from the edit bay to the production control room to "
        "the generative model.",
        "He began in post and agency video at <b>The Glitch</b> and <b>Concept "
        "Productions</b>, moved into artist and content management at <b>OML</b>, "
        "then spent five-plus years as an independent cinematographer and DOP, "
        "over a hundred branded films, OTT campaigns, episodic shows, music and "
        "fashion films, automotive and travel pieces, and social work for "
        "<b>Netflix, Meta, Dell, Mahindra, Lakmé, Gillette, Agoda</b> and many "
        "more.",
        "He traveled to London on the <b>marketing campaign for <i>83</i></b>, "
        "embedded with <b>Mumbai Indians</b> through the IPL, directed two "
        "seasons of the <b>NCPA Symphony Orchestra of India</b> live from a "
        "six-camera PCR, and designed jewellery and product creatives for U.S. "
        "house <b>Mercury Ring</b>.",
        "Today, as <b>AI Director at T-Series</b>, he handles the films end to "
        "end, from generation to direction to edit, bringing that production "
        "background into AI-led creative direction with a luxury focus.",
        "What has really changed is <b>how</b> he works: thinking in systems "
        "instead of single shots, and pairing years of production and "
        "marketing experience with generative pipelines. <b>The craft is "
        "the same.</b> The difference is that one person can now make a "
        "lot more of it.",
    ],
}

# --- Work: client-facing verticals (compartments) -------------------------
#
# Each WORK item declares a `primary` vertical (the section it lives in) and a
# list of `tags` (all the facets it belongs to). The filter bar is built from
# CATEGORIES, and a chip cross-filters every section at once - so Amit can open
# (or deep-link) the site to a specific client type. `slug` is the stable id
# used to auto-resolve an uploaded still at static/img/work/<slug>.(jpg|webp|png).

CATEGORIES = [
    {
        "slug": "ai",
        "label": "AI & Generative",
        "blurb": "AI films made end to end: generation, direction and edit, "
        "kept in-house. Built for brands that want to produce more with "
        "generative pipelines.",
    },
    {
        "slug": "brands",
        "label": "Brands & Commercials",
        "blurb": "Commercials and branded films for global consumer brands, "
        "from concept to delivery.",
    },
    {
        "slug": "ott",
        "label": "Streaming & Platforms",
        "blurb": "Promos, launch films and social campaigns across Netflix, "
        "Prime Video, Hotstar, Amazon, MTV, Viu and Colors TV.",
    },
    {
        "slug": "music",
        "label": "Music & Performance",
        "blurb": "Music videos and visualisers, plus broadcast-grade live "
        "direction, including six-camera orchestral PCR calling.",
    },
    {
        "slug": "auto",
        "label": "Automotive & Travel",
        "blurb": "Long-form expedition and road films with a cinematographer’s "
        "eye for landscape, motion and machine.",
    },
    {
        "slug": "fashion",
        "label": "Fashion, Luxury & Jewellery",
        "blurb": "A luxury sensibility across jewellery, fashion and beauty: "
        "studio fashion films, lookbooks and product-led design.",
    },
    {
        "slug": "food",
        "label": "Food & Hospitality",
        "blurb": "Premium restaurant, product and menu-launch content, made "
        "for social feeds.",
    },
    {
        "slug": "live",
        "label": "Live & Sport",
        "blurb": "Embedded, fast-turnaround content and multi-camera direction "
        "for sport, events and film campaigns.",
    },
]

WORK = [
    # ---- AI & Generative (T-Series) ----
    {
        "slug": "amrit-barbarik", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gaathayein: Barbarik", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "Barbarik could have ended the Mahabharat war in a minute. So "
        "why did Krishna stop him?",
        "href": "https://youtu.be/vb9YkbRR2A4",
    },
    {
        "slug": "amrit-padmanabhaswamy", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gaathayein: Padmanabhaswamy", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "Why were Shri Padmanabhaswamy Mandir's last two vaults never "
        "opened?",
        "href": "https://youtu.be/90an5w1cueA",
    },
    {
        "slug": "dhamal", "primary": "ai", "tags": ["ai", "music"],
        "title": "Dhamal", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "An AI music video made entirely in-house, from generation to "
        "edit.",
        "href": "https://www.youtube.com/watch?v=U6kMnUTqaeQ", "feature": True,
    },
    {
        "slug": "selfmade", "primary": "ai", "tags": ["ai", "music"],
        "title": "Selfmade", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "A fully AI-generated music film, directed and cut in-house.",
        "href": "https://youtu.be/ZPQ_FViOwTY", "feature": True,
    },
    {
        "slug": "balle-balbiro", "primary": "ai", "tags": ["ai", "music"],
        "title": "Balle Balbiro Balle", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "An AI music video for Jasbir Jassi, generated and cut in-house.",
        "href": "https://youtu.be/b07AnV4KvoQ", "feature": True,
    },
    {
        "slug": "amrit-kuber", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gaathayein: Dhandevta Kuber", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "Mythology retold through generative image and video.",
        "href": "https://www.youtube.com/watch?v=OfO3CA9Yq3Y",
    },
    {
        "slug": "amrit-promo", "primary": "ai", "tags": ["ai"],
        "title": "Amrit Gaathayein: Promo", "role": "AI Director",
        "client": "T-Series", "year": "2026",
        "meta": "Promo cut for the campaign, paced and graded for the feed.",
        "href": "https://youtu.be/aeL9m0AMjeM",
    },

    # ---- Fashion, Luxury & Jewellery ----
    {
        "slug": "amit-aggarwal", "primary": "fashion", "tags": ["fashion"],
        "title": "Amit Aggarwal Fashion Film", "role": "Cinematography",
        "client": "Amit Aggarwal", "year": "2023",
        "meta": "Couture fashion film for the Indian designer.",
        "href": "https://www.instagram.com/reel/Cn51GuGgvqS/",
    },
    {
        "slug": "lakme", "primary": "fashion", "tags": ["fashion"],
        "title": "Lakmé Fashion Films", "role": "Cinematography",
        "client": "Lakmé Fashion", "year": "2023",
        "meta": "Studio fashion films for the beauty house.",
        "href": "https://www.instagram.com/reel/CqBFvsWDr-g/",
    },
    {
        "slug": "hemant-trivedi", "primary": "fashion", "tags": ["fashion"],
        "title": "Hemant Trivedi Fashion", "role": "Cinematography",
        "client": "Hemant Trivedi", "year": "",
        "meta": "Fashion film for the veteran couturier.",
        "href": "https://www.instagram.com/p/CQlq7zxl88T/",
    },

    # ---- Music & Performance ----
    {
        "slug": "bella-ciao", "primary": "music", "tags": ["music", "ott"],
        "title": "Money Heist: Bella Ciao",
        "role": "Director of Photography", "client": "Netflix", "year": "2020",
        "meta": "Official India video for the Money Heist campaign.",
        "href": "https://www.youtube.com/watch?v=0TxfLdJ24VM", "feature": True,
    },
    {
        "slug": "boya", "primary": "music", "tags": ["music"],
        "title": "Boya", "role": "Director of Photography", "client": "Boya",
        "year": "",
        "meta": "Music video shot on location at the beach.",
        "href": "https://www.youtube.com/watch?v=3GDfcWQNbIY",
    },
    {
        "slug": "chalta-hai", "primary": "music", "tags": ["music"],
        "title": "Chalta Hai", "role": "Cinematography",
        "client": "Shalmali Kholgade · 2XSideB", "year": "",
        "meta": "Music visualiser for the Shalmali Kholgade release.",
        "href": "https://youtu.be/qJXqMFABwBE",
    },
    {
        "slug": "hungama-maroon5", "primary": "music", "tags": ["music", "live"],
        "title": "Honor Live & Loud, Maroon 5", "role": "Cinematography",
        "client": "Hungama", "year": "",
        "meta": "Live concert film, shot in Singapore and India.",
        "href": "https://youtu.be/zGdVaKEqDtQ",
    },
    {
        "slug": "yamaha-cfx", "primary": "music", "tags": ["music"],
        "title": "Yamaha Music CFX", "role": "Director",
        "client": "Yamaha Music · Canopy Media", "year": "2026",
        "meta": "Lead director on a concert-grand performance film.",
        "href": "https://www.youtube.com/watch?v=4ivn9xaNn3w", "feature": True,
    },
    {
        "slug": "soi", "primary": "music", "tags": ["music", "live"],
        "title": "Symphony Orchestra of India", "role": "Director · PCR, 6-camera",
        "client": "NCPA · SOI", "year": "2025–26",
        "meta": "Directed two seasons of India's national orchestra live from a "
        "six-camera PCR, calling cuts in real time.",
        "href": "https://www.instagram.com/symphonyorchestra_india/reels/",
    },

    # ---- Brands & OTT ----
    {
        "slug": "meta", "primary": "brands", "tags": ["brands"],
        "title": "Meta Campaign", "role": "Cinematography", "client": "Meta",
        "year": "",
        "meta": "Digital commercial for the campaign.",
        "href": "https://youtu.be/Nf8H6MNKMYE",
    },
    {
        "slug": "netflix-govt", "primary": "ott", "tags": ["ott"],
        "title": "Netflix × Govt. of India", "role": "Director of Photography",
        "client": "Netflix", "year": "",
        "meta": "Outdoor campaign film from a seven-film series.",
        "href": "https://youtu.be/kBD2Dfr4rek",
    },
    {
        "slug": "buzzfeed", "primary": "brands", "tags": ["brands"],
        "title": "BuzzFeed India", "role": "Director of Photography",
        "client": "BuzzFeed India", "year": "",
        "meta": "<i>If Opinions Were Sold Like Clothes</i>, shot on location.",
        "href": "https://youtu.be/8sdRN6aMmwM",
    },
    {
        "slug": "godaddy", "primary": "brands", "tags": ["brands"],
        "title": "GoDaddy", "role": "Cinematography", "client": "GoDaddy",
        "year": "",
        "meta": "Green-screen digital commercial.",
        "href": "https://youtu.be/mNY8RD2xAxo",
    },
    {
        "slug": "dell-futurist", "primary": "brands", "tags": ["brands"],
        "title": "Dell Futurist", "role": "Cinematography", "client": "Dell",
        "year": "",
        "meta": "On-location sound-studio commercial.",
        "href": "https://www.youtube.com/watch?v=0aA_OYV4GAI",
    },
    {
        "slug": "jubilee", "primary": "ott", "tags": ["ott"],
        "title": "Jubilee", "role": "Cinematography · Social",
        "client": "Prime Video", "year": "2023",
        "meta": "Promo content for the Prime Video period drama.",
        "href": "https://www.instagram.com/reel/CqqIgIdBHku/",
    },
    {
        "slug": "taaza-khabar", "primary": "ott", "tags": ["ott"],
        "title": "Taaza Khabar", "role": "Promo · Cinematography",
        "client": "Hotstar", "year": "2023",
        "meta": "Social promo for the Hotstar series with Bhuvan Bam.",
        "href": "https://www.instagram.com/reel/CmDpu_Wontg/",
    },
    {
        "slug": "afsos", "primary": "ott", "tags": ["ott"],
        "title": "Afsos Premiere", "role": "Event Videography",
        "client": "Prime Video · OML", "year": "2020",
        "meta": "Filmed the Mumbai launch for the OML series.",
        "href": "https://www.youtube.com/watch?v=IjhPJm9aBrU",
    },
    {
        "slug": "paisa-vasool", "primary": "ott", "tags": ["ott"],
        "title": "The Paisa Vasool Show", "role": "Producer · Cinematography",
        "client": "Viu Originals", "year": "",
        "meta": "Produced and shot eleven episodes for Viu Originals.",
        "href": "https://www.youtube.com/playlist?list=PLNoppEJMkKSrZ1Pmj3pZIUF-vZn0xaJi3",
    },
    {
        "slug": "rex-talk", "primary": "ott", "tags": ["ott"],
        "title": "MTV Rex Talk", "role": "Team Producer · DOP",
        "client": "MTV · Durex", "year": "",
        "meta": "Fourteen episodes of branded entertainment for MTV.",
        "href": "https://www.youtube.com/playlist?list=PLR-SQWFj8UefEKrRyyWbFWg3hAM1kT3o0",
    },
    {
        "slug": "mind-your-business", "primary": "ott", "tags": ["ott"],
        "title": "Mind Your Business", "role": "Cinematography · Green Screen",
        "client": "Amazon", "year": "2022",
        "meta": "Green-screen founder films for the Great Indian Festival.",
        "href": "https://www.instagram.com/reel/CjA2y2zKT8A/",
    },
    {
        "slug": "selfie-challenge", "primary": "ott", "tags": ["ott"],
        "title": "MTV Great Selfie Challenge", "role": "Team Producer · DOP",
        "client": "MTV", "year": "",
        "meta": "Filmed a travel series across India, seven episodes.",
        "href": "https://www.youtube.com/playlist?list=PL0TdAxSg6OewhnNp4yIgUA9oJnMeODwU2",
    },
    {
        "slug": "bachke-rehna", "primary": "ott", "tags": ["ott"],
        "title": "Bachke Rehna Re Baba", "role": "Cinematography · Social",
        "client": "Netflix", "year": "",
        "meta": "Social campaign film for the Netflix India release.",
        "href": "https://youtu.be/z2y48uist-o",
    },
    {
        "slug": "colors-tv", "primary": "ott", "tags": ["ott"],
        "title": "Colors TV Films", "role": "Cinematography",
        "client": "Colors TV", "year": "2023",
        "meta": "Three short promotional documentaries.",
        "href": "https://www.instagram.com/reel/CuzFdqmtllH/",
    },
    {
        "slug": "bholaa", "primary": "ott", "tags": ["ott"],
        "title": "Bholaa", "role": "Promo · Cinematography",
        "client": "T-Series", "year": "2023",
        "meta": "Social films for the theatrical and music release.",
        "href": "https://www.instagram.com/reel/CozD7HmDUtt/",
    },
    {
        "slug": "letters-to-netflix", "primary": "ott", "tags": ["ott"],
        "title": "Letters to Netflix", "role": "Cinematography",
        "client": "Netflix", "year": "",
        "meta": "Social campaign film for Netflix India.",
        "href": "https://www.instagram.com/tv/CKdTxpUoTyH/",
    },
    {
        "slug": "netflix-mumbai-mask", "primary": "ott", "tags": ["ott"],
        "title": "Money Heist: City Mask", "role": "Cinematography",
        "client": "Netflix", "year": "",
        "meta": "Mumbai city film for the Money Heist campaign.",
        "href": "https://www.instagram.com/tv/CUCCMYMKvHK/",
    },
    {
        "slug": "netflix-mom-bff", "primary": "ott", "tags": ["ott"],
        "title": "Netflix: Mom vs BFF", "role": "Director of Photography",
        "client": "Netflix", "year": "",
        "meta": "Social campaign film for the platform.",
        "href": "https://www.youtube.com/watch?v=CKFoO7EgMw4",
    },
    {
        "slug": "netflix-singles-day", "primary": "ott", "tags": ["ott"],
        "title": "Netflix: Singles Day", "role": "Cinematography",
        "client": "Netflix", "year": "",
        "meta": "Singles-day social film.",
        "href": "https://youtu.be/kpaw7bcNVp0",
    },
    {
        "slug": "whats-on-netflix", "primary": "ott", "tags": ["ott"],
        "title": "What's on Netflix", "role": "Cinematographer · Vox-pop",
        "client": "Netflix", "year": "",
        "meta": "Shot the vox-pop segments across the series.",
        "href": "https://www.youtube.com/watch?v=8GrNoVevMNI&list=PLkF7RYTIPWdfHMCkbVhz4mZw37U_99-jk",
    },
    {
        "slug": "gillette-venus", "primary": "brands", "tags": ["brands"],
        "title": "Gillette Venus", "role": "Filming Professional",
        "client": "Gillette Venus · Pocket Aces", "year": "2021",
        "meta": "Beauty-brand social film.",
        "href": "https://youtu.be/fKHMs_lsytc",
    },
    {
        "slug": "zingbus", "primary": "brands", "tags": ["brands"],
        "title": "Zingbus TVC", "role": "Cinematography", "client": "Zingbus",
        "year": "",
        "meta": "Studio TVC.",
        "href": "https://youtu.be/b8k1QdpL2SQ",
    },
    {
        "slug": "groww", "primary": "brands", "tags": ["brands"],
        "title": "Groww Digital Studio", "role": "Cinematography",
        "client": "Groww", "year": "",
        "meta": "Digital studio-setup films.",
        "href": "https://www.youtube.com/watch?v=T8X84rLyXss",
    },

    # ---- Automotive & Travel ----
    {
        "slug": "mahindra-mojo", "primary": "auto", "tags": ["auto"],
        "title": "Mahindra Mojo: The Mountain Trail",
        "role": "Director of Photography", "client": "Mahindra", "year": "",
        "meta": "A long-form expedition film from Chandigarh to Leh.",
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
        "slug": "jk-tyre-trackstar", "primary": "auto", "tags": ["auto", "live"],
        "title": "JK Tyre: MTV Trackstar",
        "role": "Assistant Director · Camera · Edit",
        "client": "JK Tyre · MTV", "year": "",
        "meta": "A long-form motorsport reality series, eleven episodes on the "
        "road.",
        "href": "https://www.youtube.com/playlist?list=PL0TdAxSg6OewVEQHg2bK7x0Wphj4Hi-Es",
    },
    {
        "slug": "land-rover", "primary": "auto", "tags": ["auto"],
        "title": "Land Rover Discovery Sport", "role": "Cinematography",
        "client": "Land Rover", "year": "2020",
        "meta": "Shot the launch film.",
        "href": "https://www.instagram.com/p/B8lFOoBhPqX/",
    },
    {
        "slug": "re-kenny", "primary": "auto", "tags": ["auto"],
        "title": "Royal Enfield Kenny", "role": "2nd Camera · Drone",
        "client": "Royal Enfield", "year": "",
        "meta": "Motorcycle road film, camera and drone.",
        "href": "https://www.youtube.com/watch?v=IxvAkzVlMh4",
    },
    {
        "slug": "spiti-valley", "primary": "auto", "tags": ["auto"],
        "title": "Spiti Valley", "role": "Cinematography · Edit",
        "client": "Independent", "year": "",
        "meta": "Shot and cut a Himalayan travelogue series.",
        "href": "https://www.youtube.com/playlist?list=PL254tQxhqsjadYZnURKTqeYNGEtRvDMmI",
    },
    {
        "slug": "agoda", "primary": "auto", "tags": ["auto"],
        "title": "Agoda Travel", "role": "Videographer", "client": "Agoda",
        "year": "",
        "meta": "Travel reels shot on location.",
        "href": "https://www.instagram.com/reel/CkLtqonA7vq/",
    },

    # ---- Food & Hospitality ----
    {
        "slug": "akina", "primary": "food", "tags": ["food"],
        "title": "Akina, Bandra", "role": "Cinematography",
        "client": "Akina", "year": "",
        "meta": "Social food content for the Bandra flagship.",
        "href": "https://www.instagram.com/reel/Co7Y_pZoDUH/",
    },
    {
        "slug": "eu-food-show", "primary": "food", "tags": ["food"],
        "title": "European Union Food Show", "role": "Cinematography",
        "client": "European Union", "year": "",
        "meta": "Food show and recipe films.",
        "href": "https://www.instagram.com/tv/CgJZqERq7by/",
    },
    {
        "slug": "faasos-pizza-wrap", "primary": "food", "tags": ["food"],
        "title": "Faasos Pizza Wrap", "role": "Production · Food Films",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Product launch film for the QSR brand.",
        "href": "https://youtu.be/2bxD8jTEBqc", "feature": True,
    },
    {
        "slug": "faasos-wrap", "primary": "food", "tags": ["food"],
        "title": "Faasos Wrap Film", "role": "Production · Food Films",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Signature-wrap product film.",
        "href": "https://youtu.be/n_mlI95xFyI",
    },
    {
        "slug": "faasos-curfew", "primary": "food", "tags": ["food"],
        "title": "Faasos Curfew Film", "role": "Production · Food Films",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Campaign film for the QSR brand.",
        "href": "https://youtu.be/QLVCaKfDTV8",
    },
    {
        "slug": "faasos-table-tennis", "primary": "food", "tags": ["food"],
        "title": "Faasos Table Tennis Film", "role": "Production · Food Films",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Concept campaign film for the QSR brand.",
        "href": "https://youtu.be/lJD21QcRXkU",
    },
    {
        "slug": "oven-story", "primary": "food", "tags": ["food"],
        "title": "Oven Story", "role": "Videography · Photography",
        "client": "Rebel Foods", "year": "2025",
        "meta": "Menu and product marketing content.",
        "href": "https://www.instagram.com/tv/CXKya6MJevW/",
    },

    # ---- Live & Sport ----
    {
        "slug": "film-83", "primary": "live", "tags": ["live"],
        "title": "83 Film Marketing", "role": "Social Media Videographer",
        "client": "Reliance Media · London", "year": "2019",
        "meta": "Three months in London on the <i>83</i> marketing campaign.",
        "href": "https://instagram.com/83thefilm",
    },
    {
        "slug": "redbull-bcone", "primary": "live", "tags": ["live"],
        "title": "Red Bull BC One", "role": "Cinematography",
        "client": "Red Bull", "year": "",
        "meta": "Event film for the global breaking championship.",
        "href": "https://youtu.be/uY2r-1VWwGk",
    },
]

# --- Career timeline (Section 00:04) --------------------------------------

TIMELINE = [
    {
        "year": "2026",
        "title": "AI Director",
        "org": "T-Series",
        "body": "Contract, full-time. End-to-end AI-video production across "
        "music video and mythology.",
        "now": True,
    },
    {
        "year": "2025 – 26",
        "title": "Founder / Director",
        "org": "FLOWV",
        "body": "Independent creative studio: direction, cinematography, edit "
        "and production. Rebel Foods launches, Yamaha Music, NCPA SOI.",
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
        "body": "Over 100 commissions across OTT, branded film, fashion, automotive, "
        "travel, food and live. Netflix, Meta, Dell, Lakmé, Mahindra, Flipkart, "
        "Agoda and more.",
        "now": False,
    },
    {
        "year": "2017 – 18",
        "title": "Content Manager",
        "org": "Only Much Louder (OML)",
        "body": "Artist content and sponsor deals for Zakir Khan, Nishant Tanwar and "
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
    "MTV", "Prime Video", "Hotstar", "Colors TV", "Viu",
]

# --- Contact socials ------------------------------------------------------

SOCIALS = [
    {"label": "Instagram · FLOWV", "href": "https://www.instagram.com/flowvvvvv"},
    {"label": "Portfolio", "href": "https://amitdasvideography.myportfolio.com/"},
    {
        "label": "Behance",
        "href": "https://www.behance.net/collection/176241147/Homemade-Series",
    },
    {"label": "Vimeo", "href": "https://vimeo.com/showcase/3366175"},
]

CONTACT = {
    "cue": "End Card · Let’s Make Something",
    "big": "Available to lead AI direction, creative direction, and "
    "production.",
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


def group_for(slug):
    """Return one decorated CATEGORY group (with its 1-based ``index`` among the
    non-empty groups) for the /work/<slug> page, or None if unknown/empty."""
    groups, _ = work_by_category()
    for i, g in enumerate(groups, start=1):
        if g["slug"] == slug:
            return {**g, "index": i}
    return None


def montage_frames(decorated):
    """De-duplicated still URLs for the hero montage (only items that resolve
    to a real image - YouTube auto-thumbs or uploaded stills)."""
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
