import os


def get_files() -> list[str]:
    # """ Walk the `docs_dir` and return a Files collection. """
    files: list[str] = []

    for source_dir, dirnames, filenames in os.walk("./docs", followlinks=True):
        relative_dir = os.path.relpath(source_dir, "./docs")
        dirnames.sort()

        for filename in sort_files(filenames):
            if filename == "extra.css":
                continue
            path = os.path.normpath(os.path.join(relative_dir, filename))
            # Skip README.md if an index file also exists in dir
            if filename.lower() == "readme.md" and "index.md" in filenames:
                continue
            files.append(path)

    return files


def sort_files(filenames: list[str]) -> list[str]:
    """Always sort `index` or `README` as first filename in list."""

    def key(f: str):
        if os.path.splitext(f)[0] in ["index", "README"]:
            return (0,)
        return (1, f)

    return sorted(filenames, key=key)


def get_title(path: str):
    first_line: str = ""

    with open(path) as f:
        first_line = f.readline().rstrip()

    return first_line[2:]


def main():
    files = get_files()
    nav_lines: list[str] = []
    prev_dir: str = ""

    for file in files:
        dir_name = ""
        slash_count = file.count("/")
        if slash_count == 1:
            index = file.find("/")
            dir_name = file[:index]
        if slash_count > 1:
            index1 = file.rfind("/")
            index2 = file.rfind("/", 0, index1 - 1)
            dir_name = file[index2 + 1 : index1]

        if dir_name != prev_dir:
            indent = "  " * (2 * slash_count - 1)
            nav_lines.append(indent + "- " + dir_name + ":\n")

        indent = "  " * (2 * slash_count + 1)
        title = get_title("./docs/" + file)
        nav_line = indent + "- " + title + ": " + file + "\n"
        nav_lines.append(nav_line)
        prev_dir = dir_name

    lines: list[str] = []
    with open("mkdocs.yml") as f:
        lines = f.readlines()

    nav_index = lines.index("nav:\n")
    new_lines = lines[: nav_index + 1] + nav_lines

    with open("mkdocs.yml", "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    main()
