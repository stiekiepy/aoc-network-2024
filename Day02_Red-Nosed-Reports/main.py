#!/usr/bin/env python3


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


"""62 65 67 70 73 76 75
68 71 73 76 78 78
77 80 81 82 86
44 47 48 51 53 58"""

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
    print(is_ascending(['9', '7', '6', '2', '1']))
    print(is_descending(['9', '7', '6', '2', '1']))
    print(adjacent_diff(['9', '7', '6', '2', '1']))
    # print(count_safe_reports(input_file))

# ['7', '6', '4', '2', '1'],: Safe without removing any level.
#  ['1', '2', '7', '8', '9'],: Unsafe regardless of which level is removed.
#  ['9', '7', '6', '2', '1'],: Unsafe regardless of which level is removed.
#  ['1', '3', '2', '4', '5'],: Safe by removing the second level, 3.
  #  0    1    2    3    4    len 5
#  ['8', '6', '4', '4', '1'],: Safe by removing the third level, 4.
#  ['1', '3', '6', '7', '9']: Safe without removing any level.