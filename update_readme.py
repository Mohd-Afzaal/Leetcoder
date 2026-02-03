import os
import re
from typing import Dict, List, Tuple

try:
    import requests
except ImportError:
    requests = None


README_PATH = "README.md"
SOLUTIONS_DIR = "solutions"
LEETCODE_API = "https://leetcode.com/api/problems/all/"

LANG_MAP = {
    "py": "Python",
    "cpp": "C++",
    "c": "C",
    "java": "Java",
    "js": "JavaScript",
}

FILE_PATTERN = re.compile(r"^(\d+)[-_ ].+\.(\w+)$")


def fetch_problem_map() -> Dict[int, Dict[str, str]]:
    """Fetch problem metadata from LeetCode. Fails gracefully."""
    if not requests:
        print("⚠️ requests not available, skipping LeetCode metadata")
        return {}

    print("🔄 Fetching problem metadata from LeetCode...")
    try:
        resp = requests.get(LEETCODE_API, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("stat_status_pairs", [])
    except Exception as e:
        print(f"❌ Failed to fetch LeetCode metadata: {e}")
        return {}

    difficulties = {1: "Easy", 2: "Medium", 3: "Hard"}
    problem_map = {}

    for entry in data:
        stat = entry.get("stat", {})
        diff = entry.get("difficulty", {})
        prob_id = stat.get("frontend_question_id")

        if not prob_id:
            continue

        problem_map[prob_id] = {
            "title": stat.get("question__title", f"Problem {prob_id}"),
            "difficulty": difficulties.get(diff.get("level"), "?"),
            "url": f"https://leetcode.com/problems/{stat.get('question__title_slug', '')}/",
        }

    print(f"✅ Loaded metadata for {len(problem_map)} problems")
    return problem_map


def scan_solutions(problem_map: Dict[int, Dict[str, str]]) -> List[Tuple]:
    """Scan solutions directory and build solution rows."""
    if not os.path.isdir(SOLUTIONS_DIR):
        print(f"⚠️ '{SOLUTIONS_DIR}' directory not found")
        return []

    solutions = []

    for root, _, files in os.walk(SOLUTIONS_DIR):
        for file in files:
            match = FILE_PATTERN.match(file)
            if not match:
                continue

            number, ext = match.groups()
            number = int(number)

            meta = problem_map.get(number, {})
            title = meta.get("title", f"Problem {number}")
            difficulty = meta.get("difficulty", "?")
            url = meta.get("url", "#")

            lang = LANG_MAP.get(ext.lower(), ext.upper())

            solutions.append(
                (number, title, difficulty, lang, "✅", url)
            )

    solutions.sort(key=lambda x: x[0])
    print(f"📂 Found {len(solutions)} solution(s)")
    return solutions


def build_table(solutions: List[Tuple]) -> str:
    header = (
        "| # | Problem | Difficulty | Language | Status |\n"
        "|---|----------|------------|----------|--------|\n"
    )

    if not solutions:
        return header + "| - | No solutions yet | - | - | - |\n"

    rows = [
        f"| {num} | [{title}]({url}) | {diff} | {lang} | {status} |"
        for num, title, diff, lang, status, url in solutions
    ]

    return header + "\n".join(rows)


def update_readme(table: str) -> None:
    if not os.path.exists(README_PATH):
        print("❌ README.md not found, skipping update")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start = "<!-- START_TABLE -->"
    end = "<!-- END_TABLE -->"

    if start in content and end in content:
        new_content = re.sub(
            rf"{start}.*?{end}",
            f"{start}\n{table}\n{end}",
            content,
            flags=re.S,
        )
        print("📝 Updated existing table")
    else:
        new_content = (
            content
            + "\n\n## 📊 Progress Tracker\n"
            + f"{start}\n{table}\n{end}\n"
        )
        print("📝 Added new progress tracker section")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    problem_map = fetch_problem_map()
    solutions = scan_solutions(problem_map)
    table = build_table(solutions)
    update_readme(table)
    print("🎉 README update complete")


if __name__ == "__main__":
    main()
