import os
import random
import html
import subprocess

GH = "gh"
ASKER = os.environ.get("ASKER", "traveler")
ISSUE = os.environ.get("ISSUE", "0")
TITLE = os.environ.get("TITLE", "a question")

FORTUNES = [
    "A merge conflict will teach you patience you did not ask for.",
    "Your next commit will break prod. Ship it anyway. The stars insist.",
    "Soon, a semicolon you forgot will reveal a bug you feared.",
    "You will refactor twice. The second time is for your sanity, not the code.",
    "A wildcard DNS record points at opportunity. Follow the CNAME.",
    "Your backlog is haunted. Not by bugs. By decisions you avoided.",
    "An untracked file holds the answer. git add it and believe.",
    "You will fix in 5 minutes what you procrastinated for 5 days.",
    "Someone, somewhere, is grateful for a comment you wrote years ago.",
    "Roll the dice on a rewrite. The universe loves chaos, but keep backups.",
    "A dark mode user will visit your profile. You are being watched. Wave.",
    "The bug is not in your code. It is in the meeting about your code.",
    "Deploy on Friday. Live dangerously. Tell them the genie approved it.",
    "Your next idea arrives in the shower. Keep a waterproof notebook.",
]

fortune = random.choice(FORTUNES)
asker_esc = html.escape(ASKER)
fortune_esc = html.escape(fortune)
title_esc = html.escape(TITLE[:52])

# wrap long fortunes onto max 2 lines (~52 chars each)
words = fortune_esc.split(" ")
line1, line2 = fortune_esc, ""
if len(fortune_esc) > 52:
    line1, line2 = "", ""
    cur = ""
    for w in words:
        if len(cur) + len(w) > 52:
            break
        cur = (cur + " " + w).strip()
    line1 = cur
    line2 = fortune_esc[len(cur):].strip()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="220" viewBox="0 0 850 220">
  <defs>
    <linearGradient id="y2kbg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff0fc"/>
      <stop offset="50%" stop-color="#eafaff"/>
      <stop offset="100%" stop-color="#f6ffe8"/>
    </linearGradient>
    <radialGradient id="orb" cx="38%" cy="30%" r="85%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#ffb3ec"/>
      <stop offset="75%" stop-color="#8fd8ff"/>
      <stop offset="100%" stop-color="#c0a4ff"/>
    </radialGradient>
  </defs>
  <rect width="850" height="220" fill="url(#y2kbg)"/>
  <g>
    <circle cx="170" cy="105" r="70" fill="url(#orb)"/>
    <circle cx="170" cy="105" r="70" fill="none" stroke="#ff9de2" stroke-width="3"/>
    <ellipse cx="150" cy="76" rx="22" ry="10" fill="#ffffff" opacity="0.75">
      <animate attributeName="opacity" values="0.5;0.9;0.5" dur="2s" repeatCount="indefinite"/>
    </ellipse>
    <path d="M118 172 Q170 190 222 172 L206 196 Q170 206 134 196 Z" fill="#e2e8f5"/>
    <text x="170" y="116" text-anchor="middle" font-size="26">🔮</text>
  </g>
  <rect x="280" y="36" rx="14" width="540" height="150" fill="#ffffff" opacity="0.88" stroke="#ffb3ec" stroke-width="2"/>
  <text x="302" y="68" font-family="Verdana" font-size="13.5" fill="#00b8e0">✦ @{asker_esc} asked:</text>
  <text x="302" y="92" font-family="Verdana" font-size="14" font-weight="bold" fill="#7a5fb8">"{title_esc}"</text>
  <text x="302" y="126" font-family="Verdana" font-size="13.5" fill="#e24fb4">the orb says: {line1}</text>
  {f'<text x="302" y="147" font-family="Verdana" font-size="13.5" fill="#e24fb4">{line2}</text>' if line2 else ''}
  <text x="302" y="176" font-family="Consolas, monospace" font-size="11" fill="#00c8ff">wish #{ISSUE} granted · forever ✧</text>
  <text x="812" y="46" font-size="15" fill="#ff6ec7">✦<animate attributeName="opacity" values="0.2;1;0.2" dur="1.5s" repeatCount="indefinite"/></text>
  <text x="824" y="190" font-size="12" fill="#00c8ff">✧<animate attributeName="opacity" values="1;0.2;1" dur="1.9s" repeatCount="indefinite"/></text>
</svg>
'''

with open("assets/crystal-ball.svg", "w", encoding="utf-8") as f:
    f.write(svg)

comment = f"""✦ **The Wish Orb has heard you, @{ASKER}.**

> {fortune}

Your wish has been carved into the [profile orb](https://github.com/nxi5) for all eternity (or until someone else makes a wish).
Close this issue — the orb has spoken. 🔮
"""

with open("comment.md", "w", encoding="utf-8") as f:
    f.write(comment)

subprocess.run(
    [GH, "issue", "comment", ISSUE, "--repo", "nxi5/nxi5", "--body-file", "comment.md"],
    check=True,
)
print("wish granted to", ASKER)
