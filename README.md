# Strategically Lazy Doll (Claude Code skill)

Turn yourself into a pretty doll and your customers' pain into memes they forward to their friends.

One image + one savage line. Every line starts from a joke that already went viral. It keeps the shape word for word and swaps the nouns into your business, so you never guess what's funny.

By Aziza Azimova · [askaze.com](https://askaze.com)
Using ChatGPT instead of Claude Code? The copy-paste version is on the resources page at askaze.com.

## Install (2 minutes)

**Option A: use it right here.**
```bash
git clone https://github.com/azemediaxyz/strategically-lazy-doll.git
cd strategically-lazy-doll
pip install pillow
claude
```
Then say: **"make me a doll meme"**.

**Option B: add it to your own project.** Copy `.claude/skills/lazy-doll-memes/` into your project's `.claude/skills/` folder, run `pip install pillow`, and say "make me a doll meme".

The first time, it interviews you (7 questions) and saves `lazy-doll-profile.yml`. Put 2 clear photos of yourself in the folder and tell it the file names.

## What it does
1. **Steals a viral line.** It picks from 30 proven joke shapes (with view counts) and rewrites them for your customer, swapping only the nouns.
2. **Culls hard.** You see the best 5–8 lines, each next to the original it came from.
3. **Makes the doll.** It writes the image prompt for your photos and scene. If an image tool is connected (Artlist, an image API) it makes the image. If not, you paste the prompt into ChatGPT or Gemini with your photos.
4. **Checks the face.** It rejects images where the eyes, face or skin tone changed.
5. **Adds the text.** `overlay.py` writes the line on the image: 1080×1350, white with a black outline, no word left alone on a line.
6. **Saves it** with a caption.

Optional: with vidIQ or Apify connected, it finds fresh viral lines on its own.

## What's inside
```
.claude/skills/lazy-doll-memes/
  SKILL.md          the method (6 steps)
  setup.md          first-run interview
  joke-shapes.md    30 proven viral joke shapes with views
  image-prompt.md   doll-look master prompt, scenes, face check
  overlay.py        puts the line on the image
profile-template.yml        your profile (the interview fills it)
examples/before-after.md    viral original → business version
```

## Rules that keep it working
- Steal the shape, not the joke. Same setup, same twist, same last beat; swap the nouns only.
- Mean beats nice. "Sounds good" means it failed.
- Only your own face (or someone who said yes).
- Don't write "Barbie" anywhere public (trademark). It's a doll.
