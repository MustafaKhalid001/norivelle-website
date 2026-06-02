import os

css_path = r"css\styles.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

target = """@media (max-width: 768px) {
  .job-card { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
}"""

replacement = """@media (max-width: 768px) {
  .job-card { flex-direction: column; align-items: flex-start; gap: 1.2rem; }
  .job-tags { flex-wrap: wrap; gap: 0.8rem; }
  .job-card .btn { font-size: 0.85rem; padding: 10px 16px; width: 100%; text-align: center; }
}"""

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("CSS updated successfully!")
else:
    print("Target string not found!")
