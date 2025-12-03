def get_file_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().splitlines()