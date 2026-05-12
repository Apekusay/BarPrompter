# BarPrompter — Mac Menu Bar Prompt Refiner

A lightweight Mac menu bar app that refines your rough prompts using DeepSeek AI. Works system-wide — any app, any window, not just your browser. Type garbage, get back a clear, actionable prompt instantly.

## How it works

1. Type your rough prompt anywhere (Claude Desktop, VS Code, Notion, Slack, anywhere)
2. Select it and copy — `⌘C`
3. Click **✦** in the menu bar
4. Click **"Refine copied prompt"**
5. Watch the icon change: **✦ → ⟳ → ✓**
6. Paste the refined prompt — `⌘V`
7. Want it even sharper? Click **"Refine again"** for another pass!

---

## Setup

**1. Install dependencies**
```bash
pip install rumps pyperclip openai
```

**2. Get a DeepSeek API key**
- Sign up at [platform.deepseek.com](https://platform.deepseek.com)
- Go to API Keys → Create new key
- New accounts get 5 million free tokens (no credit card required)

**3. Add your API key**

Open `prompt_refiner.py` and replace line 18:
```python
API_KEY = "YOUR_DEEPSEEK_API_KEY"  # ← paste your key here
```

**4. Run the app**
```bash
cd /path/to/BarPrompter
python3 prompt_refiner.py
```

A **✦** icon appears in your menu bar (top right). That's it.

> **Note:** On first run, macOS may ask for **Notifications** permission — allow it so the app can alert you of errors.

---

## Visual indicator

The menu bar icon tells you what's happening at a glance:

| Icon | Meaning |
|------|---------|
| ✦ | Ready |
| ⟳ | Refining your prompt… |
| ✓ | Done — paste with ⌘V |

---

## Refine again

Not happy with the first result? Click **"Refine again"** to run another pass on the refined prompt. Each pass makes it sharper and more precise.

Simple prompts usually peak at pass 2. Complex prompts (technical specs, creative briefs) can improve through 3-4 passes.

---

## Why BarPrompter?

Unlike browser extensions that only work inside Chrome or Safari, BarPrompter works **everywhere on your Mac** — any app, any window, any context. It lives quietly in your menu bar and is always one click away.

---

## Cost

Using DeepSeek V4 Flash at $0.14/M input + $0.28/M output tokens:
- Each refinement ≈ 200 tokens total
- 100 refinements/day ≈ $0.001/day
- Effectively free for personal use

---

## Run at login (optional)

To have BarPrompter start automatically when you log in:

**1. Find your Python path:**
```bash
which python3
```

**2. Create the launch agent** (replace both placeholders below):
```bash
mkdir -p ~/Library/LaunchAgents

cat > ~/Library/LaunchAgents/com.barprompter.plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.barprompter</string>
    <key>ProgramArguments</key>
    <array>
        <string>/YOUR/PYTHON/PATH</string>
        <string>/YOUR/PATH/TO/prompt_refiner.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF
```

Replace:
- `/YOUR/PYTHON/PATH` with the output of `which python3`
- `/YOUR/PATH/TO/prompt_refiner.py` with the full path to your file

**3. Load it:**
```bash
launchctl load ~/Library/LaunchAgents/com.barprompter.plist
```

> **Note:** On first login launch, macOS will ask for **Local folder access** and **Input Monitoring** permissions — allow both.

---

## Requirements

- macOS
- Python 3.x
- DeepSeek API key (free tier available)

---

## Issues & contributions

Found a bug or want to improve BarPrompter? Open an issue or submit a pull request on [GitHub](https://github.com/Apekusay/BarPrompter).

---

## License

MIT — free to use, modify, and share. Credit appreciated!
