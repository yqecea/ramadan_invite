import re

html_path = 'ramadan-mubarak.html'
css_path = 'style-mubarak.css'

# 1. Update HTML fonts
with open(html_path, 'r') as f:
    html = f.read()

html = re.sub(
    r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]+"\s+rel="stylesheet">',
    r'<link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@100..900&family=Geist:wght@100..900&family=Pixelify+Sans:wght@400..700&display=swap" rel="stylesheet">',
    html
)
html = re.sub(r'style-mubarak\.css\?v=\d+', 'style-mubarak.css?v=10', html)

with open(html_path, 'w') as f:
    f.write(html)

# 2. Update CSS
with open(css_path, 'r') as f:
    css = f.read()

# Replace variables with Vercel Dark Mode
vercel_vars = """    --bg: #000000;
    --bg-card: #0a0a0a;
    --accent: #ffffff;
    --accent-light: rgba(255, 255, 255, 0.15);
    --text: #ededed;
    --text-muted: #888888;
    --border: #333333;

    --ff-main: 'Geist', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --ff-tech: 'Geist Mono', 'Courier New', monospace;
    --ff-pixel: 'Pixelify Sans', monospace;"""

css = re.sub(r'    --bg:.*?(?=\})', vercel_vars + '\n', css, flags=re.DOTALL)

# Re-brand the main title to use Pixel font
css = re.sub(
    r'(\.title-main\s*\{[^}]+font-family:\s*)var\(--ff-main\)',
    r'\1var(--ff-pixel)',
    css
)

# Fix invert image for dark mode
css = re.sub(
    r'(\.illustration-img\s*\{[^}]+)mix-blend-mode:\s*multiply;',
    r'\1filter: invert(1) hue-rotate(180deg) contrast(1.2); mix-blend-mode: screen;',
    css
)
css = re.sub(
    r'(\.ornament-img\s*\{[^}]+)mix-blend-mode:\s*multiply;',
    r'\1filter: invert(1) opacity(0.5); mix-blend-mode: screen;',
    css
)

# Make countdown numbers use Geist Mono or Pixel
css = re.sub(
    r'(\.timer-value\s*\{[^}]+font-family:\s*)var\(--ff-[^)]+\)',
    r'\1var(--ff-pixel)',
    css
)
# Add terminal styling to timer blocks
css = re.sub(
    r'(\.timer-value\s*\{[^}]+)border:\s*2px\s+solid\s+var\(--olive\);',
    r'\1border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(0,0,0,0.5);',
    css
)

# Global Grid inverted
css = re.sub(
    r'(background-image:\s*linear-gradient\([^,]+,\s*rgba\()11,\s*12,\s*12(,\s*0\.04\)\s*1px,\s*transparent\s*1px\),\s*linear-gradient\([^,]+,\s*rgba\()11,\s*12,\s*12(,\s*0\.04\)\s*1px,\s*transparent\s*1px\);)',
    r'\1 255, 255, 255 \2 255, 255, 255 \3',
    css
)

# Button style to match Vercel (White bg, black text)
css = re.sub(
    r'(\.btn-primary\s*\{[^}]+background:\s*)var\(--accent\)(;\n\s*color:\s*)var\(--bg\)',
    r'\1#ffffff\2#000000',
    css
)
css = re.sub(
    r'(\.btn-primary:hover\s*\{[^}]+background:\s*)transparent(;\n\s*color:\s*)var\(--accent\)',
    r'\1#000000\2#ffffff',
    css
)
# Change border from --olive to --accent
css = css.replace('var(--olive)', 'var(--accent)')
css = css.replace('var(--gold)', 'var(--text-muted)')

with open(css_path, 'w') as f:
    f.write(css)

