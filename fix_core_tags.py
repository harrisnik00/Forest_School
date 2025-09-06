import re
from pathlib import Path

# Folder where your HTML files are
html_folder = Path("templates")

# Regex to find {% core '...' %}
pattern = re.compile(r"\{\%\s*core\s*['\"]([^'\"]+)['\"]\s*\%\}")

# Replacement: /core/<filename>
for html_file in html_folder.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    new_text = pattern.sub(r"/core/\1", text)
    html_file.write_text(new_text, encoding="utf-8")
    print(f"Processed {html_file}")
