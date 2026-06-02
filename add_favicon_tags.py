import os
import glob

# HTML to inject
favicon_tag = '    <link rel="icon" type="image/png" href="favicon.png">\n'

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if 'href="favicon.png"' not in content:
        # Insert right after <head>
        content = content.replace("<head>", "<head>\n" + favicon_tag)
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

print("Favicon tag injected into all HTML files.")
