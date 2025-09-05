import os
import re
import requests

README_PATH = "README.md"
SOLUTIONS_DIR = "solutions"  # change if needed
LEETCODE_API = "https://leetcode.com/api/problems/all/"

def fetch_problem_map():
    """Fetch problem metadata from LeetCode (id -> difficulty + slug)."""
    resp = requests.get(LEETCODE_API, timeout=10)
    data = resp.json()["stat_status_pairs"]

    difficulties = {1: "Easy", 2: "Medium", 3: "Hard"}
    problem_map = {}
    for entry in data:
        stat = entry["stat"]
        prob_id = stat["frontend_question_id"]
        slug = stat["question__title_slug"]
        difficulty = difficulties[entry["difficulty"]["level"]]
        title = stat["question__title"]
        url = f"https://leetcode.com/problems/{slug}/"
        problem_map[prob_id] = {
            "title": title,
            "difficulty": difficulty,
            "url": url,
        }

    return problem_map

def get_solutions(problem_map):
    """Scan solution files and extract problem info from filenames."""
    solutions = []
    pattern = re.compile(r"(\d+)[-_ ](.+)\.(\w+)$")

    for file in os.listdir(SOLUTIONS_DIR):
        match = pattern.match(file)
        if match:
            number, _, lang = match.groups()
            number = int(number)
            meta = problem_map.get(number, {})
            title = meta.get("title", f"Problem {number}")
            difficulty = meta.get("difficulty", "?")
            url = meta.get("url", "#")
            lang = lang.capitalize()
            solutions.append((number, title, difficulty, lang, "✅", url))

    return sorted(solutions, key=lambda x: x[0])

def update_readme(solutions):
    """Update README.md with a fresh progress table."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Build new table
    table_header = "| # | Problem | Difficulty | Language | Status |\n|---|----------|------------|----------|---------|\n"
    table_rows = "\n".join(
        f"| {num} | [{title}]({url}) | {difficulty} | {lang} | {status} |"
        for num, title, difficulty, lang, status, url in solutions
    )
    new_table = table_header + table_rows

    # Replace old table (between markers) or append if missing
    if "<!-- START_TABLE -->" in readme and "<!-- END_TABLE -->" in readme:
        import re
        readme = re.sub(
            r"<!-- START_TABLE -->(.*?)<!-- END_TABLE -->",
            f"<!-- START_TABLE -->\n{new_table}\n<!-- END_TABLE -->",
            readme,
            flags=re.S,
        )
    else:
        readme += f"\n\n## 📊 Progress Tracker\n<!-- START_TABLE -->\n{new_table}\n<!-- END_TABLE -->\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

if __name__ == "__main__":
    problem_map = fetch_problem_map()
    sols = get_solutions(problem_map)
    update_readme(sols)
