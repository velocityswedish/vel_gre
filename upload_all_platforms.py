"""
Velocity Greek - Unified Social Media Upload Script
Uploads generated reels to all connected social media platforms
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Add upload directory to Python path
upload_dir = Path(__file__).parent / "upload"
if upload_dir.exists() and str(upload_dir) not in sys.path:
    sys.path.insert(0, str(upload_dir))

# Import individual uploaders
upload_to_facebook = None
upload_to_instagram = None

try:
    from upload_facebook import upload_to_facebook as fb_upload
    upload_to_facebook = fb_upload
except ImportError as e:
    print(f"[!] Facebook upload module not available: {e}")

try:
    from upload_instagram import upload_to_instagram as ig_upload
    upload_to_instagram = ig_upload
except ImportError as e:
    print(f"[!] Instagram upload module not available: {e}")


def get_latest_reel():
    """Find the most recently generated reel"""
    video_dir = Path("output/video")

    if not video_dir.exists():
        print("❌ Δεν βρέθηκε output/video directory")
        return None

    reels = list(video_dir.glob("*/final_reel.mp4"))

    if not reels:
        print("❌ Δεν βρέθηκαν reels στο output/video directory")
        return None

    latest = max(reels, key=lambda p: p.stat().st_mtime)

    metadata_file = latest.parent / "metadata.json"
    metadata = {}
    if metadata_file.exists():
        with open(metadata_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)

    return {
        "video_path": str(latest),
        "metadata": metadata,
        "category": metadata.get("category_greek", "Ελληνικά"),
        "phrases": metadata.get("phrases", [])
    }


def generate_caption(phrases, category, platform="facebook"):
    """Generate social media caption from phrases - NO ASTERISKS, LOWERCASE HASHTAGS"""

    if platform == "facebook":
        # Longer, more engaging Facebook caption (NO ASTERISKS)
        caption_lines = [
            f"🇬🇷 Μάθετε Ελληνικά με το Velocity Greek! 🇬🇷",
            f"",
            f"📚 Κατηγορία: {category}",
            f"",
            f"🎯 Μάθετε Ελληνικά μία φράση τη φορά! Το σημερινό μάθημα {category}:",
            f""
        ]

        # Add all phrases with emojis
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
        for i, phrase in enumerate(phrases[:5], 0):
            emoji = emojis[i] if i < len(emojis) else f"{i+1}."
            caption_lines.append(f"{emoji} {phrase['english']}")
            caption_lines.append(f"   📍 {phrase['greek']}")
            caption_lines.append(f"   🔊 [{phrase.get('pronunciation', '')}]")
            caption_lines.append("")

        # Call to action (NO ASTERISKS)
        caption_lines.extend([
            f"💡 Συμβουλή: Επαναλάβετε κάθε φράση δυνατά 3 φορές!",
            f"👍 Κάντε like αν μάθατε κάτι νέο!",
            f"💬 Σχολιάστε την αγαπημένη σας φράση!",
            f"🔔 Ακολουθήστε για καθημερινά μαθήματα Ελληνικών!",
            f"",
            f"📖 Οδηγός Προφοράς:",
            f"   Η φωνητική ορθογραφία σε αγκύλες σας βοηθά να το πείτε σωστά!",
            f"",
        ])

        # Hashtags for Facebook (ALL LOWERCASE)
        hashtags = [
            "#learngreek",
            "#greeklessons",
            "#greekforbeginners",
            "#languagelearning",
            "#greekvocabulary",
            "#velocitygreek",
            "#dailygreek",
            "#greekgrammar",
            "#learnlanguages",
            "#greekteacher",
            "#speakgreek",
            "#greekpractice",
            "#bilingual",
            "#greekwords",
            "#languagetips",
            "#ελληνικά",
            "#μάθετεελληνικά",
            "#ελληνικήγλώσσα",
            "#ελλάδα"
        ]

        caption_lines.extend(hashtags)

    else:
        # Standard caption for other platforms (NO ASTERISKS, LOWERCASE HASHTAGS)
        caption_lines = [
            f"🇬🇷 Μάθετε Ελληνικά με το Velocity Greek! 🇬🇷",
            f"",
            f"Κατηγορία: {category}",
            f"",
            f"Οι σημερινές φράσεις:",
            f""
        ]

        for i, phrase in enumerate(phrases[:3], 1):
            caption_lines.append(f"{i}. {phrase['english']}")
            caption_lines.append(f"   → {phrase['greek']}")
            caption_lines.append("")

        hashtags = [
            "#learngreek",
            "#greeklessons",
            "#greekforbeginners",
            "#languagelearning",
            "#greekvocabulary",
            "#velocitygreek",
            "#dailygreek",
            "#greekgrammar",
            "#learnlanguages",
            "#greekteacher",
            "#ελληνικά",
            "#μάθετεελληνικά"
        ]

        caption_lines.extend(hashtags)

    return "\n".join(caption_lines)


def upload_to_all_platforms(video_path, caption, category):
    """Upload to all configured social media platforms with comprehensive summary"""

    results = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "video": video_path,
        "uploads": {},
        "platforms_attempted": [],
        "platforms_successful": [],
        "platforms_skipped": [],
        "platforms_failed": []
    }

    print("\n" + "="*80)
    print("🚀 VELOCITY GREEK - MULTI-PLATFORM UPLOAD")
    print("="*80)
    print(f"Video: {video_path}")
    print(f"Category: {category}")
    print(f"Caption length: {len(caption)} characters")
    print("="*80)

    if not Path(video_path).exists():
        print(f"❌ Το αρχείο βίντεο δεν βρέθηκε: {video_path}")
        return results

    platforms = [
        ("facebook", upload_to_facebook, "📘 Facebook"),
        ("instagram", upload_to_instagram, "📸 Instagram"),
    ]

    for platform_name, upload_func, display_name in platforms:
        print(f"\n{display_name} UPLOAD...")
        results["platforms_attempted"].append(platform_name)

        if upload_func:
            try:
                upload_result = None

                if platform_name == "facebook":
                    upload_result = upload_func(
                        video_path=video_path,
                        description=caption,
                        title=f"Greek: {category}"
                    )
                elif platform_name == "instagram":
                    upload_result = upload_func(
                        video_path=video_path,
                        caption=caption,
                        is_story=False
                    )

                if upload_result:
                    results["uploads"][platform_name] = upload_result
                    results["platforms_successful"].append(platform_name)
                    print(f"✅ {display_name} upload successful")
                else:
                    results["uploads"][platform_name] = {"status": "failed", "error": "Upload function returned None"}
                    results["platforms_failed"].append(platform_name)
                    print(f"❌ {display_name} upload failed: No result returned")

            except Exception as e:
                error_msg = str(e)
                results["uploads"][platform_name] = {"status": "failed", "error": error_msg}
                results["platforms_failed"].append(platform_name)
                print(f"❌ {display_name} upload failed: {error_msg}")
        else:
            print(f"⚠️  {display_name} upload skipped (module not available)")
            results["uploads"][platform_name] = {"status": "skipped", "reason": "Module not available"}
            results["platforms_skipped"].append(platform_name)

    # ===== BEAUTIFUL SUMMARY =====
    print("\n" + "="*80)
    print("📊 UPLOAD SUMMARY")
    print("="*80)

    total_attempted = len(results["platforms_attempted"])
    successful_count = len(results["platforms_successful"])
    failed_count = len(results["platforms_failed"])
    skipped_count = len(results["platforms_skipped"])

    print(f"\n📈 Overall Status:")
    print(f"   ├─ Total Platforms: {total_attempted}")
    print(f"   ├─ ✅ Successful: {successful_count}")
    print(f"   ├─ ❌ Failed: {failed_count}")
    print(f"   └─ ⚠️  Skipped: {skipped_count}")

    if total_attempted > 0:
        success_rate = (successful_count / total_attempted) * 100
        print(f"\n🎯 Success Rate: {success_rate:.0f}%")

    if results["platforms_successful"]:
        print(f"\n✅ SUCCESSFUL UPLOADS ({len(results['platforms_successful'])}):")
        for platform in results["platforms_successful"]:
            platform_data = results["uploads"].get(platform, {})
            video_id = platform_data.get("video_id", "N/A")
            print(f"   ✅ {platform.upper()}: Success (Video ID: {video_id})")

    if results["platforms_failed"]:
        print(f"\n❌ FAILED UPLOADS ({len(results['platforms_failed'])}):")
        for platform in results["platforms_failed"]:
            platform_data = results["uploads"].get(platform, {})
            error = platform_data.get("error", "Unknown error")
            print(f"   ❌ {platform.upper()}: Failed - {error[:80]}...")

    if results["platforms_skipped"]:
        print(f"\n⚠️  SKIPPED PLATFORMS ({len(results['platforms_skipped'])}):")
        skipped_list = ", ".join([p.upper() for p in results["platforms_skipped"]])
        print(f"   ⚠️  {skipped_list}")
        print(f"   💡 Add credentials to enable these platforms")

    print("\n" + "="*80)

    results_file = Path("output") / f"upload_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    results_file.parent.mkdir(exist_ok=True)
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Results saved: {results_file}")
    print("="*80)

    return results


def main():
    """Main upload workflow"""

    print("\n" + "="*80)
    print("🇬🇷 VELOCITY GREEK - AUTOMATED UPLOAD 🇬🇷")
    print("="*80)

    reel = get_latest_reel()

    if not reel:
        print("\n❌ Δεν βρέθηκε reel! Τρέξτε πρώτα το facebook_reels_automation.py")
        sys.exit(1)

    print(f"\n✅ Found latest reel:")
    print(f"   Category: {reel['category']}")
    print(f"   Video: {reel['video_path']}")
    print(f"   Phrases: {len(reel['phrases'])}")

    caption = generate_caption(reel['phrases'], reel['category'], platform="facebook")
    print(f"\n📝 Generated caption ({len(caption)} chars):")
    print("-"*80)
    print(caption[:500] + "..." if len(caption) > 500 else caption)
    print("-"*80)

    results = upload_to_all_platforms(
        reel['video_path'],
        caption,
        reel['category']
    )

    results["phrases"] = reel['phrases']

    successful = len(results.get("platforms_successful", []))
    failed = len(results.get("platforms_failed", []))
    skipped = len(results.get("platforms_skipped", []))

    if successful > 0:
        print(f"\n✅ Upload complete! {successful} platform(s) successful.")
        if skipped > 0:
            print(f"💡 {skipped} platform(s) skipped - προσθέστε credentials για ενεργοποίηση")
        sys.exit(0)
    elif failed > 0:
        print(f"\n⚠️  All attempted uploads failed ({failed} failed, {skipped} skipped).")
        print("💡 Ελέγξτε τα παραπάνω μηνύματα σφάλματος και επαληθεύστε τα credentials")
        sys.exit(1)
    else:
        print(f"\n⚠️  All uploads skipped ({skipped} skipped).")
        print("💡 Προσθέστε credentials στα GitHub Secrets για ενεργοποίηση")
        sys.exit(1)


if __name__ == "__main__":
    main()
