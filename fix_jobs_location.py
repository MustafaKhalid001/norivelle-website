import os

file_path = "careers.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace specifically in the job-tags area
content = content.replace("Lahore (Hybrid)", "Lahore (On-site)")
content = content.replace("Remote (Global)", "Lahore (On-site)")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Job locations updated successfully!")
