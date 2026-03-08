import re

def update_css(filepath):
    with open(filepath, 'r') as f:
        css = f.read()

    # 1. Heavily aggressive Main Title
    css = re.sub(
        r"(\.title-main\s*\{[^}]+font-weight:\s*)900(;\n\s*color:\s*var\(--accent\);\n\s*line-height:\s*0\.9;\n\s*letter-spacing:\s*)-0\.04em",
        r"\1 900\2-0.08em",
        css
    )
    
    # 2. Hero Date
    css = re.sub(
        r"(\.hero-date\s*\{[^}]+letter-spacing:\s*)2px",
        r"\1-1px",
        css
    )
    
    # 3. Label text tight kerning
    css = re.sub(
        r"(\.bar-label\s*\{[^}]+letter-spacing:\s*)0\.05em",
        r"\1-0.02em",
        css
    )

    with open(filepath, 'w') as f:
        f.write(css)

update_css('style-mubarak.css')
