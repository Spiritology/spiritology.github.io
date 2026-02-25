#!/usr/bin/env python3
"""
Spiritology — Quick Account Setup Assistant
Opens all signup pages and helps you set up accounts fast.
Run: python3 quick_signup.py
"""
import subprocess
import time
import sys

BRAND = "Spiritology"
WEBSITE = "https://spiritology.github.io/"
ASSESSMENT = "https://spiritology.github.io/assessment"

PLATFORMS = {
    "Instagram": {
        "signup_url": "https://www.instagram.com/accounts/emailsignup/",
        "username": "spiritology.official",
        "bio": "The Science of Inner Transformation\n🔬 Evidence-based consciousness training\n🌍 30,000+ graduates · 72 countries\n👇 Free Assessment:",
        "link": ASSESSMENT,
    },
    "Twitter/X": {
        "signup_url": "https://x.com/i/flow/signup",
        "username": "Spiritology",
        "bio": "The Science of Inner Transformation | Evidence-based consciousness training | 30,000+ graduates across 72 countries | Founded by Dr. Elias Voss | Free assessment 👇",
        "link": ASSESSMENT,
    },
    "TikTok": {
        "signup_url": "https://www.tiktok.com/signup",
        "username": "spiritology",
        "bio": "The Science of Inner Transformation 🔬 30,000+ graduates worldwide",
        "link": ASSESSMENT,
    },
    "Reddit": {
        "signup_url": "https://www.reddit.com/register/",
        "username": "Spiritology_Official",
        "bio": "The Science of Inner Transformation. Evidence-based consciousness training founded by Dr. Elias Voss. 30,000+ graduates across 72 countries.",
        "link": ASSESSMENT,
    },
    "Pinterest": {
        "signup_url": "https://www.pinterest.com/",
        "username": "SpiritologyOfficial",
        "bio": "Spiritology — The Science of Inner Transformation. Evidence-based consciousness training combining neuroscience, contemplative traditions, and energy science. Founded by Dr. Elias Voss. 30,000+ graduates across 72 countries. Free Consciousness Assessment available at spiritology.github.io",
        "link": ASSESSMENT,
    },
    "YouTube": {
        "signup_url": "https://www.youtube.com/",
        "username": "Spiritology",
        "bio": "Spiritology — The Science of Inner Transformation\n\nEvidence-based consciousness training combining neuroscience, contemplative traditions, and energy science.\n\nFounded by Dr. Elias Voss | 30,000+ graduates across 72 countries\n\nFree Consciousness Assessment: spiritology.github.io/assessment",
        "link": ASSESSMENT,
    },
}

def copy_to_clipboard(text):
    """Copy text to macOS clipboard"""
    process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def open_url(url):
    """Open URL in default browser"""
    subprocess.run(['open', url], check=True)

def main():
    print("=" * 60)
    print("  SPIRITOLOGY — Quick Account Setup Assistant")
    print("=" * 60)
    print()
    print("This tool will help you create accounts on all platforms.")
    print("It opens signup pages and copies bio text to your clipboard.")
    print()

    # Check if user wants to open all at once or step by step
    if "--all" in sys.argv:
        print("Opening ALL signup pages...")
        for name, info in PLATFORMS.items():
            open_url(info["signup_url"])
            time.sleep(0.5)
        print("\nAll pages opened! Use the bio info below for each platform.\n")
        for name, info in PLATFORMS.items():
            print(f"\n{'─' * 40}")
            print(f"  {name}")
            print(f"{'─' * 40}")
            print(f"  Username: {info['username']}")
            print(f"  Link: {info['link']}")
            print(f"  Bio:")
            for line in info['bio'].split('\n'):
                print(f"    {line}")
        return

    for i, (name, info) in enumerate(PLATFORMS.items(), 1):
        print(f"\n{'═' * 60}")
        print(f"  [{i}/{len(PLATFORMS)}] {name}")
        print(f"{'═' * 60}")
        print(f"\n  Username: {info['username']}")
        print(f"  Link:     {info['link']}")
        print(f"  Bio:")
        for line in info['bio'].split('\n'):
            print(f"    {line}")

        print(f"\n  Opening {name} signup page...")
        open_url(info["signup_url"])

        # Copy bio to clipboard
        copy_to_clipboard(info['bio'])
        print(f"  ✓ Bio copied to clipboard (Cmd+V to paste)")

        input(f"\n  Press ENTER when done with {name}...")

        # Copy link to clipboard for link-in-bio
        copy_to_clipboard(info['link'])
        print(f"  ✓ Link copied to clipboard: {info['link']}")

        input(f"  Press ENTER to continue to next platform...")

    print(f"\n{'═' * 60}")
    print("  ALL DONE!")
    print(f"{'═' * 60}")
    print(f"\n  ✓ All {len(PLATFORMS)} platforms set up")
    print(f"  ✓ Website: {WEBSITE}")
    print(f"  ✓ Assessment: {ASSESSMENT}")
    print(f"\n  Next step: Run the content posting schedule from")
    print(f"  marketing/LAUNCH_KIT.md")
    print()

if __name__ == "__main__":
    main()
