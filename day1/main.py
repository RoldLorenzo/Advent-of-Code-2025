def get_file_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    input = get_file_lines("./input.txt")
    
    position = 50
    
    total_zeros = 0
    total_times_through_zero = 0

    for line in input:    
        offset = int(line[1:])
        old_position = position
        
        # Adds the amount of times the arrow made a full turn.
        total_times_through_zero += int((offset - offset % 100) / 100)
        offset %= 100
        
        position += offset if line[0] == "R" else -offset
        
        # Checks if the arrow didn't go through one more 0
        # (if we were already on a 0, don't count it twice).
        if 0 >= position and old_position != 0 or position > 99:
            total_times_through_zero += 1
            
        position %= 100
        
        if position == 0:
            total_zeros += 1
    
    print("Part one:")
    print(total_zeros)
    
    print("Part two:")
    print(total_times_through_zero)
    
    