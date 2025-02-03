import os

def generate_summary(root_dir):
    summary_file = os.path.join(root_dir, "SUMMARY.md")
    with open(summary_file, "w") as f:
        f.write("# Table of contents\n\n")
        for dirpath, _, filenames in os.walk(root_dir):
            rel_dir = os.path.relpath(dirpath, root_dir)
            if rel_dir == ".":
                rel_dir = ""
            for filename in filenames:
                if filename.endswith(".md") and filename != "SUMMARY.md":
                    filepath = os.path.join(rel_dir, filename)
                    title = filename.replace(".md", "").replace("-", " ").title()
                    f.write(f"* [{title}]({filepath})\n")

generate_summary(".")
