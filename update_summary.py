import os

ROOT_DIR = "."
SUMMARY_FILE = os.path.join(ROOT_DIR, "SUMMARY.md")

def generate_summary():
    sections = {}

    # Scan for markdown files
    for dirpath, _, filenames in sorted(os.walk(ROOT_DIR)):
        rel_dir = os.path.relpath(dirpath, ROOT_DIR)
        
        # Ignore hidden folders and GitBook internal files
        if rel_dir.startswith(".") or rel_dir in [".git", "node_modules"]:
            continue
        
        md_files = sorted([f for f in filenames if f.endswith(".md") and f != "SUMMARY.md"])

        if md_files:
            section_name = rel_dir.replace("-", " ").title()  # Convert dir name to title case
            sections[section_name] = [os.path.join(rel_dir, f) for f in md_files]

    # Write new SUMMARY.md
    with open(SUMMARY_FILE, "w") as f:
        f.write("# Table of contents\n\n")

        for section, files in sections.items():
            if section != ".":
                f.write(f"## {section}\n\n")  # Write section title
            
            for file in files:
                title = os.path.basename(file).replace(".md", "").replace("-", " ")
                title = title.replace("_", " ")  # Handle underscores like in the left example
                title = title.title()  # Capitalize title as per example
                f.write(f"* [{title}]({file})\n")
            
            f.write("\n")  # Spacing between sections

if __name__ == "__main__":
    generate_summary()
    print("SUMMARY.md has been updated!")
