"""VELOCITY GREEK - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY GREEK"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "GREEK"
HANDLE = "@velocitygreek"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "el",
    "name": "Greek",
    "native_name": "Ελληνικά",
    "history_key": "greek",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "el-GR-AthinaNeural",
    "native_fallback_voice": "el-GR-NestorasNeural",
    "native_engine": "edge",
    "native_lang_code": "el",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ΕΛΛΗΝΙΚΑ",
    "translit_label": "SAY IT LIKE",
    "greeting": "Γεια σας!",
    "encouragement": "Εξαιρετικά!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "Παρακίνηση", "rocket", "#A560E8"),
    ("Love", "Αγάπη", "heart", "#FF4B4B"),
    ("Success", "Επιτυχία", "trophy", "#F5A700"),
    ("Wisdom", "Σοφία", "book", "#A560E8"),
    ("Happiness", "Ευτυχία", "smile", "#F5A700"),
    ("Self Improvement", "Αυτοβελτίωση", "leaf", "#58CC02"),
    ("Gratitude", "Ευγνωμοσύνη", "heart", "#FF7A00"),
    ("Friendship", "Φιλία", "users", "#00A889"),
    ("Hope", "Ελπίδα", "sun", "#FF7A00"),
    ("Creativity", "Δημιουργικότητα", "palette", "#E056A0"),
    ("Inner Peace", "Εσωτερική Ειρήνη", "lotus", "#00A889"),
    ("Confidence", "Αυτοπεποίθηση", "shield", "#1CB0F6"),
    ("Perseverance", "Επιμονή", "mountain", "#FF7A00"),
    ("Inspiration", "Έμπνευση", "sparkles", "#A560E8"),
    ("Positive Life", "Θετική Ζωή", "sun", "#58CC02"),
    ("Courage", "Θάρρος", "shield", "#FF4B4B"),
    ("Kindness", "Καλοσύνη", "heart", "#E056A0"),
    ("Patience", "Υπομονή", "hourglass", "#00A889"),
    ("Forgiveness", "Συγχώρεση", "hands", "#FF7A00"),
    ("Strength", "Δύναμη", "dumbbell", "#FF4B4B"),
    ("Joy", "Χαρά", "smile", "#F5A700"),
    ("Balance", "Ισορροπία", "scale", "#00A889"),
    ("Growth", "Ανάπτυξη", "sprout", "#58CC02"),
    ("Purpose", "Σκοπός", "target", "#A560E8"),
    ("Mindfulness", "Ενσυνειδητότητα", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learngreek",
    "#greeklessons",
    "#greekforbeginners",
    "#languagelearning",
    "#greekvocabulary",
    "#velocitygreek",
    "#dailygreek",
    "#greek",
    "#learnlanguages",
    "#speakgreek",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
