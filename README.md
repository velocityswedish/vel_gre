# 🇬🇷 Velocity Greek - Automated Facebook Reels Bot

**Αυτοματοποιημένη δημιουργία περιεχομένου εκμάθησης Ελληνικών για social media**

Δημιουργεί και αναρτά 4x καθημερινά στο Facebook, Instagram και άλλες πλατφόρμες με:
- ✅ Φράσεις στα Ελληνικά με AI και Αγγλικές μεταφράσεις
- ✅ Επαγγελματικό text-to-speech (Edge TTS)
- ✅ Όμορφα φόντα gradient με επικαλύψεις κειμένου
- ✅ Τέλειο συγχρονισμό ήχου-βίντεο
- ✅ Branding Velocity Greek
- ✅ **ΠΟΤΕ δεν επαναλαμβάνει φράσεις** (μόνιμη παρακολούθηση ιστορικού)

---

## 📅 Ημερήσιο Πρόγραμμα (American EST/EDT)

| Ανάρτηση | Ώρα (EST) | Ώρα (UTC) | Θέμα |
|------|------------|------------|-------|
| 1 | 9:00 ΠΜ | 14:00 UTC | Πρωινή παρακίνηση |
| 2 | 12:00 ΜΜ | 17:00 UTC | Διάλειμμα μεσημεριανού |
| 3 | 3:00 ΜΜ | 20:00 UTC | Απογευματινή ενίσχυση |
| 4 | 7:00 ΜΜ | 00:00 UTC | Βραδινή έμπνευση |

---

## 🎬 Διαθέσιμες Κατηγορίες (25 Συνολικά)

1. Motivation (Παρακίνηση)
2. Love (Αγάπη)
3. Success (Επιτυχία)
4. Wisdom (Σοφία)
5. Happiness (Ευτυχία)
6. Self Improvement (Αυτοβελτίωση)
7. Gratitude (Ευγνωμοσύνη)
8. Friendship (Φιλία)
9. Hope (Ελπίδα)
10. Creativity (Δημιουργικότητα)
11. Inner Peace (Εσωτερική Ειρήνη)
12. Confidence (Αυτοπεποίθηση)
13. Perseverance (Επιμονή)
14. Inspiration (Έμπνευση)
15. Positive Life (Θετική Ζωή)
16. Courage (Θάρρος)
17. Kindness (Καλοσύνη)
18. Patience (Υπομονή)
19. Forgiveness (Συγχώρεση)
20. Strength (Δύναμη)
21. Joy (Χαρά)
22. Balance (Ισορροπία)
23. Growth (Ανάπτυξη)
24. Purpose (Σκοπός)
25. Mindfulness (Ενσυνειδητότητα)

---

## 🚀 Εγκατάσταση GitHub Actions

### Βήμα 1: Προσθήκη Secrets στο GitHub Repository

Πηγαίνετε στο GitHub repository → Settings → Secrets and variables → Actions

**Απαραίτητα Secrets:**

```bash
# Pollinations AI (για δημιουργία περιεχομένου)
POLLINATIONS_API_KEY=sk_your_api_key_here

# Facebook (για ανέβασμα Reels)
FACEBOOK_ACCESS_TOKEN=your_token
FACEBOOK_PAGE_ID=your_page_id

# Instagram (για ανέβασμα Reels)
INSTAGRAM_ACCESS_TOKEN=your_token
INSTAGRAM_ACCOUNT_ID=your_account_id

# Προαιρετικό: Άλλες πλατφόρμες
VK_ACCESS_TOKEN=your_token
VK_GROUP_ID=your_group_id
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHANNEL_ID=your_channel_id
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_secret
```

### Βήμα 2: Ενεργοποίηση GitHub Actions

1. Πηγαίνετε στην καρτέλα Actions στο GitHub repository σας
2. Ενεργοποιήστε τα workflows αν είναι απενεργοποιημένα
3. Το workflow θα εκτελείται αυτόματα 4x καθημερινά

### Βήμα 3: Χειροκίνητη Δοκιμή

Μπορείτε να ενεργοποιήσετε χειροκίνητα το workflow:
1. Πηγαίνετε Actions → "Velocity Greek - Daily 4x Upload"
2. Κάντε κλικ "Run workflow"
3. Επιλέξτε branch (main/master)
4. Κάντε κλικ "Run workflow"

---

## 💻 Τοπική Δοκιμή

### Προαπαιτούμενα

```bash
# Εγκαταστήστε Python 3.11+
# Εγκαταστήστε FFmpeg
# Εγκαταστήστε dependencies
pip install -r requirements.txt
```

### Δημιουργία Single Reel

```bash
python facebook_reels_automation.py
```

### Δημιουργία Ημερήσιου Περιεχομένου (4 reels)

```bash
python -c "from facebook_reels_automation import generate_daily_content; generate_daily_content(times_per_day=4)"
```

### Ανέβασμα στα Social Media

```bash
cd upload
python ../upload_all_platforms.py
```

---

## 📁 Δομή Project

```
Velocity Greek/
├── .env                              # API keys και credentials
├── .github/
│   └── workflows/
│       └── daily_4x_upload.yml      # GitHub Actions workflow
├── facebook_reels_automation.py     # Κύριο script δημιουργίας
├── upload_all_platforms.py          # Ενοποιημένο script upload
├── upload/
│   ├── upload_facebook.py
│   ├── upload_instagram.py
│   ├── upload_vk.py
│   └── ...
├── output/
│   ├── video/                       # Δημιουργημένα reels
│   ├── history/                     # Ιστορικό φράσεων (ΜΗΝ ΔΙΑΓΡΑΨΕΤΕ!)
│   └── daily_summary_*.json        # Ημερήσια logs δημιουργίας
└── requirements.txt
```

---

## 🔧 Διαμόρφωση

### Ρύθμιση Timezone

Το workflow χρησιμοποιεί EST/EDT (UTC-5). Για αλλαγή timezone:

1. Επεξεργαστείτε το `.github/workflows/daily_4x_upload.yml`
2. Τροποποιήστε τα cron schedules:
   ```yaml
   # Για PST (UTC-8):
   - cron: '0 17 * * *'  # 9 ΠΜ PST
   - cron: '0 20 * * *'  # 12 ΜΜ PST
   - cron: '0 23 * * *'  # 3 ΜΜ PST
   - cron: '0 3 * * *'   # 7 ΜΜ PST
   ```

### Συχνότητα Ανάρτησης

Για αλλαγή από 4x σε 3x καθημερινά:

1. Επεξεργαστείτε το `.github/workflows/daily_4x_upload.yml`
2. Αφαιρέστε ένα cron schedule
3. Ενημερώστε `generate_daily_content(times_per_day=3)` στο script

---

## 🎨 Προδιαγραφές Βίντεο

- **Ανάλυση:** 1080x1920 (9:16 κάθετο)
- **Μορφή:** MP4 (H.264 + AAC)
- **Διάρκεια:** ~30-50 δευτερόλεπτα (5 φράσεις)
- **Frame Rate:** 30 FPS
- **Ήχος:** Edge TTS (GuyNeural EN, AthinaNeural EL)

---

## 📊 Ιστορικό Φράσεων

Όλες οι δημιουργημένες φράσεις αποθηκεύονται στο:
```
output/history/all_generated_phrases.json
```

**Αυτό το αρχείο είναι ΜΟΝΙΜΟ και δεν πρέπει ΠΟΤΕ να διαγραφεί.**

Εξασφαλίζει:
- ✅ Καμία φράση δεν επαναλαμβάνεται ποτέ
- ✅ Φρέσκο περιεχόμενο κάθε μέρα
- ✅ Παρακολούθηση όλου του δημιουργημένου περιεχομένου

---

## 🐛 Αντιμετώπιση Προβλημάτων

### Αποτυχία Δημιουργίας Βίντεο

```bash
# Έλεγχος εγκατάστασης FFmpeg
ffmpeg -version

# Επαναεγκατάσταση αν χρειάζεται
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```

### Αποτυχία Upload Ήχου

```bash
# Έλεγχος αρχείου .env
cat .env | grep FACEBOOK
cat .env | grep INSTAGRAM

# Επαλήθευση εγκυρότητας tokens
# Δημιουργήστε ξανά αν έχουν λήξει
```

### Αποτυχία GitHub Actions

1. Ελέγξτε τα logs στην καρτέλα Actions
2. Επαληθεύστε ότι όλα τα secrets έχουν οριστεί σωστά
3. Ελέγξτε τα artifact uploads για δημιουργημένα αρχεία
4. Αναθεωρήστε τα logs για συγκεκριμένα μηνύματα σφάλματος

---

## 📈 Μετρικές Απόδοσης

- **Χρόνος Δημιουργίας:** ~2-3 λεπτά ανά reel
- **Χρόνος Upload:** ~1-2 λεπτά ανά πλατφόρμα
- **Συνολικό Workflow:** ~5-10 λεπτά ανά ανάρτηση
- **Ημερήσια Χωρητικότητα:** 4 αναρτήσεις × 5 φράσεις = 20 φράσεις/ημέρα
- **Περιστροφή Κατηγοριών:** 25 κατηγορίες = 6+ ημέρες πριν την επανάληψη

---

## 🎯 Βασικά Χαρακτηριστικά

### ✅ Τέλειος Συγχρονισμός Ήχου-Βίντεο
- Κάθε εικόνα εμφανίζεται για την ακριβή διάρκεια του ήχου
- Διατήρηση χρονισμού Αγγλικά + 500ms παύση + Ελληνικά
- Χωρίς πρόωρες μεταβάσεις ή διακοπές

### ✅ Φυσική Ομιλία
- Οι φράσεις περιλαμβάνουν κόμματα για φυσικό διάλειμμα
- Παράδειγμα: "Dream big, start small"
- Το TTS ακούγεται φυσικό, όχι ρομποτικό

### ✅ Επαγγελματικός Σχεδιασμός
- Φόντα gradient πολλαπλών στάσεων
- Ξεχωριστά χρώματα: Ναυτικό (EN) / Βουργουνδί (EL) / Γκρι (Προφορά)
- Branding Velocity Greek σε κάθε καρέ

### ✅ Χωρίς Επαναλήψεις
- Μόνιμη παρακολούθηση ιστορικού φράσεων
- AI δημιουργεί φρέσκο περιεχόμενο κάθε φορά
- Έλεγχος όλων των φράσεων πριν τη δημιουργία

---

## 📞 Υποστήριξη

Για προβλήματα ή ερωτήσεις:
1. Ελέγξτε τα logs του GitHub Actions
2. Αναθεωρήστε τα μηνύματα σφάλματος στην έξοδο
3. Επαληθεύστε όλα τα διαπιστευτήρια API
4. Ελέγξτε το ιστορικό φράσεων για διπλότυπα

---

## 📄 Άδεια

Αυτό το project είναι για εκπαιδευτικούς σκοπούς. Σεβαστείτε τους όρους παροχής υπηρεσιών API της πλατφόρμας.

---

**Φτιαγμένο με ❤️ για τους μαθητές των Ελληνικών παγκοσμίως**

🇬🇷 Μάθετε Ελληνικά με το Velocity Greek! 🇬🇷
