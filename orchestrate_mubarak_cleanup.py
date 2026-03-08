import re

html_path = 'ramadan-mubarak.html'
css_path = 'style-mubarak.css'

with open(html_path, 'r') as f:
    html = f.read()

# 1. Remove HUD noise
html = re.sub(r'<div class="hud-top-left">\s*EXPERIMENTAL SYSTEMS\s*</div>', '', html)
html = re.sub(r'<div class="hud-top-right">\s*ASTANA // KAZ &nbsp;&nbsp;&nbsp; DATA_SYNC: 99% &nbsp;&nbsp;&nbsp; 2026 // V2\s*</div>', '', html)
html = re.sub(r'<div class="top-hud">\s*</div>', '', html)
html = re.sub(r'<div class="hud-corners">\s*<div.*?</div>\s*<div.*?</div>\s*<div.*?</div>\s*<div.*?</div>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div class="hud-bottom-bar">\s*<div class="hud-bottom-left">/*/*/*/*/*/*/*/*/*/*/*/*</div>\s*<div class="hud-bottom-center">RAMADAN 1447</div>\s*<div class="hud-bottom-right">/*/*/*/*/*/*/*/*/*/*/*/*</div>\s*</div>', '', html)
html = re.sub(r'<div class="hud-timer-title">\[ T-MINUS // ДО АУЫЗАШАРА \]</div>', '<div class="hud-timer-title">ДО АУЫЗАШАРА</div>', html)
html = re.sub(r'<div class="hud-contact-title">\[ КОНТАКТ \]</div>', '<div class="hud-contact-title">КОНТАКТ</div>', html)

# 2. Update specific texts
# "Ассаляму алейкум, братья! Приглашаем..." -> "Ассаляму алейкум! Приглашаем..."
html = html.replace('Ассаляму алейкум, братья!', 'Ассаляму алейкум!')

# Address gate logic
old_gate = r'<div class="detail-item">\s*<div class="detail-icon">\s*<i class="fas fa-lock"></i>\s*</div>\s*<div class="detail-text">\s*<div class="detail-label">Код домофона</div>\s*<div class="detail-value">1877# или #9757#</div>\s*</div>\s*</div>'
new_gate = '''<div class="detail-item">
            <div class="detail-icon">
                <i class="fas fa-lock"></i>
            </div>
            <div class="detail-text">
                <div class="detail-label">Код от внешней калитки</div>
                <div class="detail-value">#9757#</div>
                <div class="detail-label" style="margin-top: 5px;">Код от подъезда</div>
                <div class="detail-value">#3333</div>
            </div>
        </div>'''
html = re.sub(old_gate, new_gate, html)

# Contact info ("Ануар" is fine, but maybe change label or remove "братья/ахи")
# Contact title is already cleaned

# Replace ?v=10 to ?v=11
html = html.replace('style-mubarak.css?v=10', 'style-mubarak.css?v=11')
html = html.replace('style-mubarak.css?v=3', 'style-mubarak.css?v=11')
html = html.replace('style-mubarak.css?v=4', 'style-mubarak.css?v=11')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Make it match the Text Laboratory vibe more closely. Light mint background, very stark black text.
# The user liked `/tmp/brutal_mubarak1.png` but "чище, читабельнее".
# The previous background for `brutal_mubarak1.png` was maybe `#f0f5f1` or something.
# Let's ensure background is very light, stark colors.
css = re.sub(r'--bg:.*?(?=\})', '''    --bg: #e8f7f2;
    --bg-card: rgba(255, 255, 255, 0.7);
    --accent: #000000;
    --accent-light: rgba(0, 0, 0, 0.1);
    --text: #000000;
    --text-muted: #333333;
    --border: #000000;
    --olive: #000000;
    --gold: #000000;

    --ff-main: 'Inter', system-ui, sans-serif;
    --ff-tech: 'Share Tech Mono', monospace;''', css, flags=re.DOTALL)

# Ensure container has proper top padding without the HUD
css = re.sub(r'\.app-container\s*\{[^}]*padding:[^;]+;', 'padding: 40px 20px 80px;', css)

with open(css_path, 'w') as f:
    f.write(css)

