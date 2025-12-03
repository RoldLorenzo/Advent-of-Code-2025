# Finds the largest number of length in a list of digits 1-9.
# The digits of the resulting number have to be in order in the list,
# but not necessarily consecutive.

# Examples:
# digits = 234234234234278
# length = 2
# Returns: 78

# digits = 234234234234278
# length = 12
# Returns: 434234234278

def find_largest_number(digits: list[int], length: int) -> int:
    largest = [0 for _ in range(length)]

    for i, digit in enumerate(digits):
        for j in range(length):
            if digit > largest[j] and i + length - j <= len(digits):
                largest[j] = digit

                for k in range(j + 1, length):
                    largest[k] = 0

                break

    return list_to_int(largest)


def list_to_int(digits: list[int]) -> int:
    result = 0
    exponent = len(digits) - 1
    for digit in digits:
        result += 10 ** exponent * digit
        exponent -= 1

    return result


if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as file:
        input = [[int(digit) for digit in list(line)]
                 for line in file.read().splitlines()]

    part_one = sum(find_largest_number(line, 2) for line in input)
    print(part_one)

    part_two = sum(find_largest_number(line, 12) for line in input)
    print(part_two)
