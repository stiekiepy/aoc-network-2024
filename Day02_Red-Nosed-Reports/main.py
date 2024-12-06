#!/usr/bin/env python3

def is_ascending(levels):
    is_true = True
    for i in range(len(levels)-1):
        if int(levels[i]) < int(levels[i+1]):
            continue
        else:
            return False
    return is_true

def is_descending(levels):
    is_true = True
    pop_counter = 0
    for i in range(len(levels)-1):
        if int(levels[i]) > int(levels[i+1]):
            continue
        else:
            return False

    return is_true

def adjacent_diff(levels):
    is_True = True
    for i in range(len(levels)-1):
        if 1 <= abs(int(levels[i]) - int(levels[i+1])) <= 3:
            continue
        else:
            is_True = False
    return is_True

def count_safe_reports(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            levels = line.split()
            # print(levels)
            if is_ascending(levels) and adjacent_diff(levels):
                count += 1
            elif is_descending(levels) and adjacent_diff(levels):
                count += 1
            else:
                continue
    return count
            

if __name__ == '__main__':
    input_file = './input.txt'
    # print(is_ascending(['9', '7', '6', '2', '1']))
    # print(is_descending(['9', '7', '6', '2', '1']))
    # print(adjacent_diff(['9', '7', '6', '2', '1']))
    print(count_safe_reports(input_file))

"""
assert is_safe([7, 6, 4, 2, 1]) == 42, "Safe because the levels are all decreasing by 1 or 2."
assert is_safe([1, 2, 7, 8, 9]) == False, "Unsafe because 2 7 is an increase of 5."
assert is_safe([9, 7, 6, 2, 1]) == False, "Unsafe because 6 2 is a decrease of 4."
assert is_safe([1, 3, 2, 4, 5]) == False, "Unsafe because 1 3 is increasing but 3 2 is decreasing."
assert is_safe([8, 6, 4, 4, 1]) == False, "Unsafe because 4 4 is neither an increase or a decrease."
assert is_safe([1, 3, 6, 7, 9]) == True, "Safe because the levels are all increasing by 1, 2, or 3."
"""