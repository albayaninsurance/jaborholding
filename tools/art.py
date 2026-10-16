import json, math, os
g = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo', 'qatar.json')))
ring = g['coordinates'][0]
lon0, lat0 = 51.2, 25.3
k = math.cos(math.radians(lat0))
xs = [(x-lon0)*k for x,y in ring]; ys = [-(y-lat0) for x,y in ring]
mnx, mxx, mny, mxy = min(xs), max(xs), min(ys), max(ys)
W = 300; s = W/(mxx-mnx); H = (mxy-mny)*s
P = lambda lo, la: (((lo-lon0)*k-mnx)*s+20, (-(la-lat0)-mny)*s+20)
pts = [P(x,y) for x,y in ring]
d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts) + ' Z'
dx, dy = P(51.531, 25.285)
VW, VH = W+40, H+40
def qmap(label_doha, label_qatar):
    return f'''<svg class="qmap" style="direction:ltr" viewBox="0 0 {VW:.0f} {VH:.0f}" role="img" aria-label="{label_qatar}">
<path d="{d}" fill="#5A0F28" stroke="#A88A45" stroke-width="1.5" stroke-linejoin="round"/>
<text x="{VW*0.42:.0f}" y="{VH*0.55:.0f}" class="qn">{label_qatar}</text>
<circle cx="{dx:.1f}" cy="{dy:.1f}" r="14" fill="none" stroke="#D9C38E" stroke-width="1" opacity=".6"/>
<circle cx="{dx:.1f}" cy="{dy:.1f}" r="5.5" fill="#D9C38E"/>
<text x="{dx-22:.1f}" y="{dy+5:.1f}" text-anchor="end" class="qd">{label_doha}</text>
</svg>'''

# Doha skyline: Museum of Islamic Art on the left, West Bay (Dafna) towers on the right
S, G = '#55102A', '#A88A45'
sh = []
# MIA stepped volumes
for x0,x1,y0,y1 in [(60,260,172,210),(88,232,146,172),(112,208,118,146),(134,186,90,118),(150,170,72,90)]:
    sh.append(f'<path d="M{x0+6} {y0} H{x1-6} L{x1} {y0+6} V{y1} H{x0} V{y0+6} Z"/>')
win = f'<path d="M154 112 V102 a6 6 0 0 1 12 0 V112 Z" fill="{G}" opacity=".9"/>'
# West Bay
tw = [
 'M540 210 V120 H582 V210 Z',
 'M600 210 V62 L630 52 V210 Z', 'M640 210 V52 L670 62 V210 Z',          # Palm towers
 'M700 210 V44 Q700 22 725 18 Q750 22 750 44 V210 Z', 'M723 18 V2 h4 V18 Z',  # Doha Tower + spire
 'M762 210 V86 L800 70 V210 Z',
 'M816 210 Q852 126 816 42 H884 Q848 126 884 210 Z',                     # Tornado Tower
 'M900 210 V98 H932 V210 Z',
 'M944 210 V62 h10 v-8 h22 v8 h10 V210 Z',                              # Al Bidda
 'M1000 210 V84 L1020 64 L1040 84 V210 Z',
 'M1056 210 V112 H1096 V210 Z', 'M1108 210 V142 H1150 V210 Z', 'M480 210 V158 H526 V210 Z',
]
sh += [f'<path d="{p}"/>' for p in tw]
lights = ''.join(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="210" />' for x,y0 in [(725,60),(850,60),(965,80),(1020,96),(615,80),(655,80)])
SKY = f'''<svg class="skyline" viewBox="0 0 1200 214" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
<g fill="{S}">{''.join(sh)}</g>{win}
<g stroke="{G}" stroke-width="1.2" stroke-dasharray="2 7" opacity=".55">{lights}</g>
<path d="M1128 40 a16 16 0 1 0 14 24 a12 12 0 1 1 -14 -24 Z" fill="{G}" opacity=".8"/>
<rect x="0" y="210" width="1200" height="4" fill="{G}"/>
</svg>'''

# Opening sequence: Qatar map draws in, tilts and dives into Doha, the gate rises with the tagline
def intro(tag, name, skip):
    ox, oy = dx/VW*100, dy/VH*100
    return f'''<div class="intro" id="intro" aria-hidden="true" onclick="this.remove()">
<svg class="imap" style="direction:ltr;transform-origin:{ox:.1f}% {oy:.1f}%" viewBox="0 0 {VW:.0f} {VH:.0f}">
<path class="iland" pathLength="1" d="{d}"/>
<circle class="iring" cx="{dx:.1f}" cy="{dy:.1f}" r="16"/><circle class="ipin" cx="{dx:.1f}" cy="{dy:.1f}" r="6"/>
</svg>
<div class="icenter">
<svg class="igate" viewBox="0 0 120 120"><path d="M22 114 V62 A38 38 0 0 1 98 62 V114 Z" fill="#FAF5EF"/><line class="ibar" x1="60" y1="56" x2="60" y2="84" stroke="#A88A45" stroke-width="10" stroke-linecap="round"/></svg>
<span class="iname">{name}</span><strong class="itag">{tag}</strong>
</div>
<div class="isky">{SKY}</div>
<button class="iskip" type="button">{skip}</button>
</div>
<script>(function(){{var i=document.getElementById('intro');try{{if(sessionStorage.getItem('jh-intro')||matchMedia('(prefers-reduced-motion: reduce)').matches){{i.remove();return}}sessionStorage.setItem('jh-intro','1')}}catch(e){{}}document.addEventListener('keydown',function(){{i.remove()}},{{once:true}});setTimeout(function(){{i.remove()}},6400)}})();</script>'''
