import os

IGNORE_FILES = ["extra.css", ".DS_Store", "*.svg"]
TAB_ORDER_LIST = [
    "index.md",
    "Basic",
    "Frontend",
    "Backend",
    "DevOps",
    "Software Design",
    "Data Science",
    "Blockchain",
]


def get_files() -> list[str]:
    """Walk the `docs_dir` and return a Files collection."""
    files: list[str] = []

    for src_dir, _, filenames in os.walk("./docs", followlinks=True):
        relative_dir = os.path.relpath(src_dir, "./docs")

        for filename in sort_files(filenames):
            ext = os.path.splitext(filename)[-1]
            if ext != ".md":
                continue
            path = os.path.normpath(os.path.join(relative_dir, filename))
            files.append(path)

    return files


def sort_files(filenames: list[str]) -> list[str]:
    """Always sort `index` as first filename in list."""

    def key(f: str):
        if os.path.splitext(f)[0] == "index":
            return (0,)
        return (1, f)

    return sorted(filenames, key=key)


def get_title(path: str):
    first_line: str = ""

    with open(path) as f:
        first_line = f.readline().rstrip()

    return first_line[2:]


def sort_custom(files: list[str]) -> list[str]:
    for keyword in reversed(TAB_ORDER_LIST):
        filtered = list(filter(lambda f: f.startswith(keyword), files))
        removed = list(filter(lambda f: not f.startswith(keyword), files))
        filtered.extend(removed)
        files = filtered
    return files


def to_nav_lines(files: list[str]) -> list[str]:
    nav_lines: list[str] = []
    prev_dir: str = ""

    for file in files:
        dir_name, slash_count = get_dir_name(file)

        if dir_name != prev_dir:
            indent = "  " * (2 * slash_count - 1)
            nav_lines.append(indent + "- " + dir_name + ":\n")

        indent = "  " * (2 * slash_count + 1)
        title = get_title("./docs/" + file)
        nav_line = indent + "- " + title + ": " + file + "\n"
        nav_lines.append(nav_line)
        prev_dir = dir_name

    return nav_lines


def get_dir_name(file: str) -> tuple[str, int]:
    dir_name = ""

    slash_count = file.count("/")
    if slash_count == 1:
        index = file.find("/")
        dir_name = file[:index]
    if slash_count > 1:
        index1 = file.rfind("/")
        index2 = file.rfind("/", 0, index1 - 1)
        dir_name = file[index2 + 1 : index1]

    return dir_name, slash_count


def update_mkdocs(files: list[str]):
    nav_lines = to_nav_lines(files)

    lines: list[str] = []

    with open("mkdocs.yml") as f:
        lines = f.readlines()

    nav_index = lines.index("nav:\n")
    new_lines = lines[: nav_index + 1] + nav_lines

    with open("mkdocs.yml", "w") as f:
        f.writelines(new_lines)


def main():
    files = get_files()
    sorted_files = sort_custom(files)

    update_mkdocs(sorted_files)


if __name__ == "__main__":
    main()
