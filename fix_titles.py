# Quarto post-render step: Quarto joins page and site title with an en dash
# ("About – Filip Popovic"). Replace it with a plain separator.
import glob, re

for path in glob.glob("docs/**/*.html", recursive=True):
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    fixed = re.sub(r"<title>(.*?) – (.*?)</title>", r"<title>\1 | \2</title>", html)
    if fixed != html:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fixed)
