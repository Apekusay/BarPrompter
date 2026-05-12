"""
BarPrompter — Mac Menu Bar Prompt Refiner
Copy your rough prompt (Cmd+C), click ✦ in menu bar, click Refine.
Refined prompt is silently copied to clipboard — paste with Cmd+V.

Requirements:
    pip install rumps pyperclip openai
"""

import threading
import pyperclip
import rumps
from openai import OpenAI

# ── CONFIG ───────────────────────────────────────────────
API_KEY = "YOUR_DEEPSEEK_API_KEY"  # ← paste your key here
# ─────────────────────────────────────────────────────────

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")


def refine(text):
    r = client.chat.completions.create(
        model="deepseek-v4-flash",
        max_tokens=1024,
        messages=[
            {"role": "system", "content": "You are a prompt engineer. The user gives you a rough prompt. Rewrite it to be clear, specific and actionable. Reply with ONLY the refined prompt — no explanation, no intro, no quotes."},
            {"role": "user", "content": text}
        ]
    )
    return r.choices[0].message.content.strip()


class App(rumps.App):
    def __init__(self):
        super().__init__("✦", quit_button="Quit BarPrompter")
        self.menu = [
            rumps.MenuItem("Refine copied prompt", callback=self.refine_prompt),
            rumps.MenuItem("Refine again", callback=self.refine_prompt),
            None,
            rumps.MenuItem("How to use", callback=self.show_help),
        ]
        self._busy = False

    @rumps.clicked("Refine copied prompt")
    def refine_prompt(self, _):
        if self._busy:
            rumps.notification("BarPrompter", "Still refining…", "Please wait")
            return
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        self._busy = True
        try:
            text = pyperclip.paste().strip()
            if not text:
                self.title = "✦"
                rumps.notification("BarPrompter", "Nothing to refine", "Copy your prompt first (⌘C)")
                return
            self.title = "⟳"
            refined = refine(text)
            pyperclip.copy(refined)
            self.title = "✓"
            import threading
            def reset():
                import time
                time.sleep(3)
                self.title = "✦"
            threading.Thread(target=reset, daemon=True).start()
        except Exception as e:
            self.title = "✦"
            rumps.notification("BarPrompter", "Error", str(e))
        finally:
            self._busy = False

    @rumps.clicked("How to use")
    def show_help(self, _):
        rumps.alert(
            "How to use BarPrompter",
            "1. Type your rough prompt anywhere\n"
            "2. Select it and copy  (⌘C)\n"
            "3. Click ✦ in the menu bar\n"
            "4. Click 'Refine copied prompt'\n"
            "5. Paste the refined prompt  (⌘V)\n\n"
            "That's it — works in any app!"
        )


if __name__ == "__main__":
    if API_KEY == "YOUR_DEEPSEEK_API_KEY":
        rumps.alert("Setup needed", "Open prompt_refiner.py and paste your DeepSeek API key on line 18.")
    else:
        App().run()
