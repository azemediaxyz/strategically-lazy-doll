---
name: lazy-doll-memes
description: Make "Strategically Lazy Doll" meme posts (one pretty doll-version image of the user + one savage line about their business) built from lines that already went viral, so their audience forwards them. Use when the user says "doll meme", "lazy doll", "make a meme", "make it funnier", or asks for edgy one-liners or meme captions about their business. Runs a short setup interview the first time.
---

# Strategically Lazy Doll: memes people forward

One image (a polished, doll-like version of the user) + one savage line about the pain their customers live with. The goal: someone reads it, goes "ha, that's so me", and sends it to a friend. "Sounds good" is a fail.

## Step 0. Profile
Look for `lazy-doll-profile.yml` in the project root. If it's missing or empty, run `setup.md` first (5 minutes), save the profile, then continue. Read the profile before every run; everything below uses it.

## Step 1. Start from a line that already went viral (never write from scratch)
1. Open `joke-shapes.md` and pick 10–15 shapes that fit the user's targets and emotional core.
2. **Fresher lines (optional):** if the user has an outlier tool (vidIQ `vidiq_instagram_tiktok_outlier_search`, an Apify Instagram/TikTok scraper), search "relatable one-line text meme" for their audience, last 30–60 days, 100K+ views, and keep static one-line posts with the biggest multiples (50×+). If they paste lines they've seen, use those. Add good finds to `joke-shapes.md`.
3. Rewrite each one **keeping its structure and rhythm word for word**. Swap only the nouns: the husband/dog/kid becomes one of the profile's `targets`; the relief becomes one of the `offers` said as a result. Changing more than the nouns breaks the joke.

## Step 2. The rules every line follows
- Frame business pain through what the audience already jokes about (from `audience.what_they_joke_about`).
- Name the weight (`emotional_core`), then one beat of relief. The relief is the offer as a result; never the product name.
- Roast situations, tools, competitors and the user herself. Never a real person by name.
- Edge follows `voice.edge`. Default savage: petty, a little unhinged, never nice.
- Specific beats vague: "7 grown men", "end of day", "47 minutes".

## Step 3. Cull hard
Write 10+, show the user the best **5–8**, each next to the proven original it came from, plus a suggested scene. A line survives only if:
- someone would tag a friend in it;
- the ending is a surprise, and the funniest word is last;
- it's the shortest version that still works;
- it's specific and mean enough;
- the user would say it with a smirk.
The user picks. Note what they cut and why in the profile under `learned:` so the next round is better.

## Step 4. The image
Follow `image-prompt.md`: the master prompt with the user's 2 photos (+ optional style reference), one scene picked from the line (tired line → tired doll; petty line → calm doll in front of chaos). Generate 2. Run the face check before showing anything. If no image tool is connected, give the user the filled-in prompt to paste into ChatGPT or Gemini with their photos.

## Step 5. The text
Run `python3 overlay.py <image> "<line>" -o <output.jpg>`. It crops to 1080×1350 (4:5), and writes the line in white with a thin black outline on the bottom of the image. Use `--position top` if the bottom is busy, and put `\n` where a line break reads best (never leave one word alone on a line). Show the result.

## Step 6. Save
- Finished meme: `<output.folder>/final/<short-slug>.jpg`. Raw image without text: `<output.folder>/raw/raw-<scene>.jpg`. Keep every raw image the user didn't reject; the same image can carry a new line later.
- A caption for the post: one sentence that extends the joke + a soft CTA to the offer (e.g. "If this is you, the link in my bio does the follow-ups for you.").
- Never call it "Barbie" in public text or file names (Mattel trademark). Say doll / Strategically Lazy.
