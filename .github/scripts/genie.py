import os
import random
import html
import urllib.parse
import subprocess

GH = "gh"
ASKER = os.environ.get("ASKER", "traveler")
ISSUE = os.environ.get("ISSUE", "0")
TITLE = os.environ.get("TITLE", "a question")

FORTUNES = [
    "A merge conflict will teach you patience you did not ask for.",
    "Your next commit will break prod. Ship it anyway. The stars insist.",
    "Soon, a semicolon you forgot will reveal a bug you feared.",
    "The node modules you delete today return as errors tomorrow. Burn the cache.",
    "You will refactor twice. The second time is for your sanity, not the code.",
    "A wildcard DNS record points at opportunity. Follow the CNAME.",
    "Beware the junior who quotes StackOverflow from 2012. They wield legacy magic.",
    "Your backlog is haunted. Not by bugs. By decisions you avoided.",
    "The stars aligned on your branch. Rebase before they drift.",
    "An untracked file holds the answer. git add it and believe.",
    "You will fix in 5 minutes what you procrastinated for 5 days.",
    "Someone, somewhere, is grateful for a comment you wrote years ago.",
    "The mermaid you ignored in the docs will come back as an outage.",
    "Roll the dice on a rewrite. The universe loves chaos, but keep backups.",
    "A dark mode user will visit your profile. You are being watched. Wave.",
]

fortune = random.choice(FORTUNES)
asker_esc = html.escape(ASKER)
fortune_esc = html.escape(fortune)
title_esc = html.escape(TITLE[:60])

issue_url = f"https://github.com/nxi5/nxi5/issues/{ISSUE}"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="220" viewBox="0 0 850 220">
  <defs>
    <radialGradient id="ball" cx="38%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#e9d5ff"/>
      <stop offset="45%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#2e1065"/>
    </radialGradient>
    <filter id="spark"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="850" height="220" fill="#0a0118"/>
  <g>
    <circle cx="170" cy="110" r="72" fill="url(#ball)" opacity="0.92"/>
    <circle cx="170" cy="110" r="72" fill="none" stroke="#c4b5fd" stroke-width="2"/>
    <ellipse cx="148" cy="82" rx="20" ry="10" fill="#ffffff" opacity="0.35">
      <animate attributeName="opacity" values="0.2;0.5;0.2" dur="2.2s" repeatCount="indefinite"/>
    </ellipse>
    <path d="M120 178 Q170 195 220 178 L204 200 Q170 210 136 200 Z" fill="#3b2a63"/>
    <text x="170" y="118" text-anchor="middle" font-size="26" fill="#f5f3ff">🔮</text>
  </g>
  <text x="300" y="66" font-family="Consolas, monospace" font-size="15" fill="#7dd3fc">@{asker_esc} asked: "{title_esc}"</text>
  <text x="300" y="112" font-family="Consolas, monospace" font-size="17" font-weight="bold" fill="#e9d5ff">the genie says:</text>
  <text x="300" y="142" font-family="Consolas, monospace" font-size="14" fill="#ffffff">{fortune_esc}</text>
  <text x="300" y="180" font-family="Consolas, monospace" font-size="11" fill="#7dd3fc">fortune #{ISSUE} granted — your wish is locked in {issue_url}</text>
  <circle cx="820" cy="40" r="2" fill="#e9d5ff" filter="url(#spark)"><animate attributeName="cy" values="30;190" dur="6s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="6s" repeatCount="indefinite"/></circle>
  <circle cx="835" cy="60" r="1.5" fill="#7dd3fc" filter="url(#spark)"><animate attributeName="cy" values="50;180" dur="8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="8s" repeatCount="indefinite"/></circle>
</svg>
'''

with open("assets/crystal-ball.svg", "w", encoding="utf-8") as f:
    f.write(svg)

comment = f"""🔮 **The genie has heard you, @{ASKER}.**

> {fortune}

Your fortune has been carved into the [profile crystal ball](https://github.com/nxi5) for all eternity (or until someone else asks).
Close this issue — the genie has spoken. 🧞‍♂️
"""

with open("comment.md", "w", encoding="utf-8") as f:
    f.write(comment)

subprocess.run(
    [GH, "issue", "comment", ISSUE, "--repo", "nxi5/nxi5", "--body-file", "comment.md"],
    check=True,
)
print("fortune granted to", ASKER)
