# Returns True if the string is just two equal consecutive strings.
# Examples

# abcabc -> True
# 12312 -> False

def is_repeated(text: str) -> bool:
    text_length = len(text)
    if text_length % 2 != 0:
        return False

    half = int(text_length / 2)
    return text[0:half] == text[half:]

# Returns True if the string is a sequence of equal strings.
# Examples

# abcabc -> True
# abcabcabc -> True
# aaaaaaaaa -> True
# a -> True
# abcab -> False
# 12312 -> False


def is_sequence_of_equal_strings(text: str) -> bool:
    curr_size = 1
    text_length = len(text)
    is_sequence = True

    while curr_size <= text_length // 2:
        sub_str = text[0:curr_size]

        for j in range(curr_size, text_length, curr_size):
            if sub_str != text[j:j + curr_size]:
                is_sequence = False
                break

        if is_sequence:
            return True

        is_sequence = True
        curr_size += 1

    return False


def sum_repeated(interval: list[str]) -> int:
    sum = 0

    for num in range(interval[0], interval[1] + 1):
        if is_repeated(str(num)):
            sum += num

    return sum


def sum_repeated_sequences(interval: list[str]) -> int:
    sum = 0

    for num in range(interval[0], interval[1] + 1):
        if is_sequence_of_equal_strings(str(num)):
            sum += num

    return sum


if __name__ == "__main__":
    id_ranges = []
    with open("./input.txt", "r") as file:
        id_ranges = [
            [int(i) for i in id_range.split("-")] for id_range in file.read().split(",")
        ]

    total = sum(sum_repeated(interval) for interval in id_ranges)
    print("Part one:")
    print(total)

    day_2 = sum(sum_repeated_sequences(interval) for interval in id_ranges)
    print("Part two:")
    print(day_2)
