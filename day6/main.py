from operator import add, mul


def get_file_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    input = get_file_lines("input.txt")

    operators = input.pop().split()
    input = [[int(num) for num in line.split()] for line in input]

    total = 0

    for i, op_str in enumerate(operators):
        result = 0 if op_str == "+" else 1
        op = add if op_str == "+" else mul

        for line in input:
            result = op(result, line[i])

        total += result

    print("Part one")
    print(total)
