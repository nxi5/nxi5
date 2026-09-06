import datetime
import html
import time

now = datetime.datetime.now()
h, m, s = now.hour, now.minute, now.second

# hand angles (SVG rotate, 0 = pointing up)
hour_a = (h % 12) * 30 + m * 0.5
min_a = m * 6
sec_a = s * 6

digital = now.strftime("%H:%M:%S")
tz_label = time.tzname[0] if time.tzname else "local"
synced = now.strftime("%d %b %Y · %H:%M UTC%z")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="200" viewBox="0 0 850 200">
  <defs>
    <filter id="nglow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="850" height="200" fill="#02000d"/>
  <g transform="translate(170,100)">
    <circle r="78" fill="#0d0620" stroke="#8b5cf6" stroke-width="3"/>
    <g stroke="#a78bfa" stroke-width="2">
      <line y1="-66" y2="-72"/><line x1="33" y1="-57.2" x2="36" y2="-62.4"/><line x1="57.2" y1="-33" x2="62.4" y2="-36"/><line x1="66" x2="72"/><line x1="57.2" y1="33" x2="62.4" y2="36"/><line x1="33" y1="57.2" x2="36" y2="62.4"/><line y1="66" y2="72"/><line x1="-33" y1="57.2" x2="-36" y2="62.4"/><line x1="-57.2" y1="33" x2="-62.4" y2="36"/><line x1="-66" x2="-72"/><line x1="-57.2" y1="-33" x2="-62.4" y2="-36"/><line x1="-33" y1="-57.2" x2="-36" y2="-62.4"/>
    </g>
    <line x1="0" y1="6" x2="0" y2="-38" stroke="#ffffff" stroke-width="5" stroke-linecap="round" transform="rotate({hour_a:.1f})"/>
    <line x1="0" y1="8" x2="0" y2="-56" stroke="#e9d5ff" stroke-width="3.5" stroke-linecap="round" transform="rotate({min_a:.1f})"/>
    <line x1="0" y1="12" x2="0" y2="-64" stroke="#ff5470" stroke-width="2" stroke-linecap="round">
      <animateTransform attributeName="transform" type="rotate" from="{sec_a}" to="{sec_a + 360}" dur="60s" repeatCount="indefinite"/>
    </line>
    <circle r="4.5" fill="#ff5470"/>
    <circle r="1.8" fill="#ffffff"/>
  </g>
  <text x="290" y="70" font-family="Consolas, monospace" font-size="34" font-weight="bold" fill="#ffffff" filter="url(#nglow)">{html.escape(digital)}</text>
  <text x="290" y="100" font-family="Consolas, monospace" font-size="13" fill="#8b5cf6">this clock on this profile is REAL.</text>
  <text x="290" y="122" font-family="Consolas, monospace" font-size="13" fill="#8b5cf6">a robot re-renders it every 15 minutes,</text>
  <text x="290" y="144" font-family="Consolas, monospace" font-size="13" fill="#8b5cf6">even when nobody is watching.</text>
  <text x="290" y="176" font-family="Consolas, monospace" font-size="11" fill="#6b7280">last sync: {html.escape(synced)} ({html.escape(tz_label)})</text>
  <circle cx="270" cy="64" r="5" fill="#2ea043"><animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite"/></circle>
</svg>
'''

with open("assets/living-clock.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("clock synced:", digital)
