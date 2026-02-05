import os
import re
import json
from typing import Dict, List, Tuple
from collections import defaultdict

try:
    import requests
except ImportError:
    requests = None


README_PATH = "README.md"
SOLUTIONS_DIR = "solutions"
LEETCODE_API = "https://leetcode.com/api/problems/all/"
CACHE_FILE = "leetcode_cache.json"

LANG_MAP = {
    "py": "Python",
    "cpp": "C++",
    "c": "C",
    "java": "Java",
    "js": "JavaScript",
}

FILE_PATTERN = re.compile(r"^(\d+)[-_ ].+\.(\w+)$")


def load_cache() -> Dict[int, Dict[str, str]]:
    """Load cached LeetCode data from file."""
    if not os.path.exists(CACHE_FILE):
        print("📂 No cache file found")
        return {}
    
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"✅ Loaded {len(data)} problems from cache")
            return {int(k): v for k, v in data.items()}
    except Exception as e:
        print(f"⚠️ Failed to load cache: {e}")
        return {}


def save_cache(problem_map: Dict[int, Dict[str, str]]) -> None:
    """Save LeetCode data to cache file."""
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(problem_map, f, indent=2)
            print(f"💾 Cached {len(problem_map)} problems to {CACHE_FILE}")
    except Exception as e:
        print(f"⚠️ Failed to save cache: {e}")


def fetch_problem_map() -> Dict[int, Dict[str, str]]:
    """Fetch problem metadata from LeetCode. Falls back to cache on failure."""
    
    # Try to fetch from API
    if requests:
        print("🔄 Fetching problem metadata from LeetCode API...")
        try:
            resp = requests.get(LEETCODE_API, timeout=10)
            resp.raise_for_status()
            data = resp.json().get("stat_status_pairs", [])
            
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

            print(f"✅ Loaded metadata for {len(problem_map)} problems from API")
            
            # Save to cache for future use
            save_cache(problem_map)
            return problem_map
            
        except Exception as e:
            print(f"❌ Failed to fetch from API: {e}")
            print("📂 Falling back to cache...")
    else:
        print("⚠️ requests not available")
        print("📂 Using cache...")
    
    # Fallback to cache
    cached_data = load_cache()
    if cached_data:
        return cached_data
    
    print("❌ No cache available, continuing with empty metadata")
    return {}


def scan_solutions(problem_map: Dict[int, Dict[str, str]]) -> List[Tuple]:
    """Scan solutions directory and build solution rows."""
    if not os.path.isdir(SOLUTIONS_DIR):
        print(f"⚠️ '{SOLUTIONS_DIR}' directory not found")
        return []

    grouped = defaultdict(set)

    for root, _, files in os.walk(SOLUTIONS_DIR):
        for file in files:
            match = FILE_PATTERN.match(file)
            if not match:
                continue

            number, ext = match.groups()
            number = int(number)
            lang = LANG_MAP.get(ext.lower(), ext.upper())
            grouped[number].add(lang)

    solutions = []
    for number in sorted(grouped):
        meta = problem_map.get(number, {})
        solutions.append((
            number,
            meta.get("title", f"Problem {number}"),
            meta.get("difficulty", "?"),
            ", ".join(sorted(grouped[number])),
            "✅",
            meta.get("url", "#")
        ))

    print(f"📂 Found {len(solutions)} problem(s)")
    return solutions


def build_table(solutions: List[Tuple]) -> str:
    header = (
        "| # | Problem | Difficulty | Languages | Status |\n"
        "|---|----------|------------|-----------|--------|\n"
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