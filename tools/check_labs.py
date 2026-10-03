"""Generate the course site navigation data and check the lab content.

Usage:
    python tools/check_labs.py          # run all checks (used by CI)
    python tools/check_labs.py --write  # regenerate _data/course.yml, then run all checks

Course settings (sections, groups, Learn links, getting-started page) live in
_data/course_config.yml. The navigation data in _data/course.yml is generated from the
lab files, so titles, exercises, minutes, and file links have one source: the Markdown.

Errors fail the check. Warnings point out content to tidy up but don't fail it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "_data" / "course_config.yml"
DATA = ROOT / "_data" / "course.yml"

EXERCISE = re.compile(r"^##\s+Exercise\s+(\d+)\s*[:.\-\u2013\u2014]?\s*(.+?)\s*$", re.M | re.I)
MINUTES = re.compile(r"Estimated\s+time[^\n\d]{0,40}?(\d+)\s*minutes", re.I)
MD_LINK = re.compile(r"!?\[[^\]]*\]\(<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^\s*(```|~~~)(\S*)")
LABEL = re.compile(r"^\s*(?:Lab|Demo)\s*0*(\d+)\b", re.I)
IMAGE = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def load_config() -> dict:
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8"))


def repo_url_pattern(config: dict) -> re.Pattern:
    repo = re.escape(config["github_repo"])
    return re.compile(
        rf"https://(?:raw\.githubusercontent\.com/{repo}/(?:refs/heads/)?([\w.\-]+)/"
        rf"|github\.com/{repo}/(?:blob|raw|tree)/([\w.\-]+)/)([^\s)\"'`>]+)")


def front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def minutes(value) -> int | None:
    match = re.search(r"\d+", str(value or ""))
    return int(match.group()) if match else None


def section_files(section: dict) -> list[Path]:
    excluded = set(section.get("exclude", []))
    return sorted(p for p in ROOT.glob(section["glob"]) if p.name not in excluded)


def exercises_of(body: str) -> list[dict]:
    heads = list(EXERCISE.finditer(body))
    result = []
    for index, head in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(body)
        found = MINUTES.search(body, head.end(), end)
        result.append({"number": int(head.group(1)), "title": head.group(2).strip(),
                       "minutes": int(found.group(1)) if found else None})
    return result


def file_refs(path: Path, body: str, config: dict) -> tuple[list[str], list[str]]:
    """Return repo files a page links to (not Markdown or images) and link targets that don't exist."""
    files, missing = [], []
    for target in MD_LINK.findall(body):
        if target.startswith(("http://", "https://", "#", "mailto:", "{{")):
            continue
        resolved = (path.parent / target.split("#")[0].split("?")[0]).resolve()
        if not resolved.exists():
            missing.append(target)
        elif resolved.is_file() and resolved.suffix.lower() not in IMAGE | {".md"}:
            item = rel(resolved)
            if item not in files:
                files.append(item)
    for _, _, repo_path in repo_url_pattern(config).findall(body):
        repo_path = repo_path.split("#")[0].split("?")[0].rstrip(".,;")
        target = ROOT / repo_path
        if not target.exists():
            missing.append(repo_path)
        elif target.is_file() and target.suffix.lower() not in IMAGE | {".md"} and repo_path not in files:
            files.append(repo_path)
    return files, missing


def build_data(config: dict) -> dict:
    sections = []
    for section in config["sections"]:
        key = section["front_matter_key"]
        groups = [dict(g, items=[]) for g in section.get("groups", [])]
        default = {"title": section.get("default_group", section["title"]), "items": []}
        position = 0
        for path in section_files(section):
            meta, body = front_matter(path)
            info = meta.get(key) or {}
            if not info.get("title"):
                continue
            position += 1
            title = str(info["title"]).strip()
            number = LABEL.match(title)
            files, _ = file_refs(path, body, config)
            item = {
                "file": rel(path),
                "url": "/" + rel(path)[:-3] + ".html",
                "label": f"{section['item_label']} {int(number.group(1)) if number else position}",
                "title": title,
                "description": str(info.get("description") or "").strip(),
                "minutes": minutes(info.get("duration")),
                "level": info.get("level"),
                "exercises": [{k: e[k] for k in ("title", "minutes")} for e in exercises_of(body)],
                "files": files,
            }
            module = str(info.get("module") or "")
            target = next((g for g in groups if g.get("match") and g["match"].lower() in module.lower()), None)
            target = target or next((g for g in groups if g.get("default")), None)
            (target or default)["items"].append(item)
        if default["items"]:
            groups.append(default)
        clean = [{"title": g["title"], "learn_url": g.get("learn_url", ""),
                  "minutes": sum(i["minutes"] or 0 for i in g["items"]), "items": g["items"]}
                 for g in groups if g["items"]]
        sections.append({"id": section["id"], "title": section["title"], "item_label": section["item_label"],
                         "groups": clean})
    return {"getting_started": config.get("getting_started", ""), "sections": sections}


def dump(data: dict) -> str:
    header = "# Generated by tools/check_labs.py --write from the lab files. Don't edit by hand.\n"
    return header + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=200)


def check(config: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    for section in config["sections"]:
        key = section["front_matter_key"]
        paths = section_files(section)
        if not paths:
            errors.append(f"Section '{section['title']}': no files match {section['glob']}")
        group_matches = [g["match"] for g in section.get("groups", []) if g.get("match")]
        for path in paths:
            meta, body = front_matter(path)
            info = meta.get(key) or {}
            for field in section.get("required", ["title", "description", "duration"]):
                if not info.get(field):
                    errors.append(f"{rel(path)}: front matter {key}.{field} is missing")
            if group_matches and not any(m.lower() in str(info.get("module", "")).lower() for m in group_matches):
                warnings.append(f"{rel(path)}: {key}.module doesn't match a group in _data/course_config.yml")
            exercises = exercises_of(body)
            numbers = [e["number"] for e in exercises]
            if numbers and numbers != list(range(1, len(numbers) + 1)):
                warnings.append(f"{rel(path)}: exercises aren't numbered 1..{len(numbers)}")
            timed = [e["minutes"] for e in exercises if e["minutes"] is not None]
            total = minutes(info.get("duration"))
            if timed and len(timed) == len(exercises) and total and sum(timed) != total:
                warnings.append(f"{rel(path)}: exercise minutes add up to {sum(timed)}, but {key}.duration is {total}")

    pattern = repo_url_pattern(config)
    default_branch = config.get("default_branch", "main")
    for path in sorted((ROOT / "Instructions").rglob("*.md")) + [ROOT / "index.md"]:
        _, body = front_matter(path)
        _, missing = file_refs(path, body, config)
        for target in missing:
            errors.append(f"{rel(path)}: link target doesn't exist in the repo: {target}")
        for raw_branch, blob_branch, repo_path in pattern.findall(body):
            branch = raw_branch or blob_branch
            if branch != default_branch:
                warnings.append(f"{rel(path)}: link to {repo_path} uses branch '{branch}', not '{default_branch}'")
        if "<!--" in body:
            warnings.append(f"{rel(path)}: contains an HTML comment, which is published in the page source")
        inside, unlabeled = None, 0
        for line in body.splitlines():
            fence = FENCE.match(line)
            if fence:
                if inside is None:
                    inside = fence.group(1)
                    unlabeled += 0 if fence.group(2) else 1
                elif fence.group(1) == inside:
                    inside = None
        if unlabeled:
            warnings.append(f"{rel(path)}: {unlabeled} code block(s) without a language, such as powershell or text")

    start = config.get("getting_started")
    if start and not (ROOT / start).is_file():
        errors.append(f"{start} is missing")
    if not DATA.is_file() or DATA.read_text(encoding="utf-8").replace("\r\n", "\n") != dump(build_data(config)):
        errors.append("_data/course.yml is out of date. Run: python tools/check_labs.py --write")
    return errors, warnings


def main() -> int:
    config = load_config()
    if "--write" in sys.argv:
        DATA.write_text(dump(build_data(config)), encoding="utf-8", newline="\n")
        print(f"Wrote {rel(DATA)}")
    errors, warnings = check(config)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    count = sum(len(section_files(s)) for s in config["sections"])
    print(f"{count} pages checked: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
