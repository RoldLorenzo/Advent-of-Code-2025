def get_fresh_ids(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    sum = 0

    for id in ids:
        for (start, end) in ranges:
            if start <= id <= end:
                sum += 1
                break

    return sum


if __name__ == "__main__":
    ranges = []
    ids = []

    with open("input.txt", "r") as file:
        [ranges_raw, ids_raw] = file.read().split("\n\n", 1)
        for line in ranges_raw.splitlines():
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        ids = list(map(int, ids_raw.splitlines()))

    fresh_ids = get_fresh_ids(ranges, ids)

    print("Part one")
    print(fresh_ids)
