from util import get_file_lines


def in_range(matrix: list[list[any]], pos: tuple[int, int]) -> bool:
    return (
        0 <= pos[0] < len(matrix) and
        0 <= pos[1] < len(matrix[0])
    )


def count_neighbours(matrix: list[list[str]], pos: tuple[int, int]) -> int:
    amnt_neighbours = 0

    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1] - 1, pos[1] + 2):
            if (i, j) != pos and in_range(matrix, (i, j)) and matrix[i][j] == "@":
                amnt_neighbours += 1

    return amnt_neighbours


def find_accessible_rolls(matrix: list[list[str]]) -> int:
    accessible_rolls = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@" and count_neighbours(matrix, (i, j)) < 4:
                accessible_rolls.add((i, j))

    return accessible_rolls


def remove_accessible(matrix: list[list[str]]) -> int:
    accessible_rolls = find_accessible_rolls(matrix)
    amnt_removed = len(accessible_rolls)

    for (i, j) in accessible_rolls:
        matrix[i][j] = "."

    return amnt_removed


def total_removed(matrix):
    amnt_removed = 0

    while True:
        removed_this_time = remove_accessible(matrix)
        amnt_removed += removed_this_time

        if removed_this_time == 0:
            break

    return amnt_removed


if __name__ == "__main__":
    input = get_file_lines(
        "C:/Desktop/programacao/Python/advent_of_code_2025/day4/input.txt")
    input = list(map(list, input))

    print("Part one")
    print(len(find_accessible_rolls(input)))
    print("Part two")
    print(total_removed(input))
