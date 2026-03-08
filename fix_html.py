import re

with open('ramadan-mubarak.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove top hud
html = re.sub(r'<div class="top-hud">.*?</div>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div class="hud-top-left">.*?</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div class="hud-top-right">.*?</div>', '', html, flags=re.DOTALL)

# Remove corners
html = re.sub(r'<div class="hud-corners">.*?</div>\s*</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)
# Actually the corners might be <div class="hud-corners">...</div>
html = re.sub(r'<div class="hud-corners">.*?</div>', '', html, flags=re.DOTALL)

# Bottom bars
html = re.sub(r'<div class="hud-bottom-bar">.*?</div>', '', html, flags=re.DOTALL)

# Timer title
html = re.sub(r'\[\s*T-MINUS\s*//\s*ДО\s*АУЫЗАШАРА\s*\]', 'ДО АУЫЗАШАРА', html)

# Contact title
html = re.sub(r'\[\s*КОНТАКТ\s*\]', 'КОНТАКТ', html)

# Gate code
old_gate = r'<div class="detail-label">Код домофона</div>\s*<div class="detail-value">1877# или #9757#</div>'
new_gate = r'<div class="detail-label">Код от внешней калитки</div>\n                            <div class="detail-value" style="font-family: var(--ff-tech); font-size: 1.1rem; letter-spacing: 1px;">#9757#</div>\n                            <div class="detail-label" style="margin-top: 10px;">Код от подъезда</div>\n                            <div class="detail-value" style="font-family: var(--ff-tech); font-size: 1.1rem; letter-spacing: 1px;">#3333</div>'

html = re.sub(old_gate, new_gate, html, flags=re.DOTALL)

# Image blend mode
html = html.replace('style="mix-blend-mode: multiply;"', '') # wait, we need multiply for both images to merge with the mint green
# The CSS needs to be updated.

with open('ramadan-mubarak.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style-mubarak.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add multiply blend mode to images to remove white bg
css = re.sub(r'(\.illustration-img\s*\{[^}]+)', r'\1 mix-blend-mode: multiply;', css)
# If it already had multiply, this might duplicate it, let's just forcefully replace
css = re.sub(r'mix-blend-mode:\s*multiply;\s*mix-blend-mode:\s*multiply;', 'mix-blend-mode: multiply;', css)

with open('style-mubarak.css', 'w', encoding='utf-8') as f:
    f.write(css)

