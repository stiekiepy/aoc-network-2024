#!/usr/bin/env python3

"""
Can't get this one to work yet
"""

def adjacent_diff(levels):
    for i in range(len(levels)-1):
        if 1 <= abs(int(levels[i]) - int(levels[i+1])) <= 3:
            continue
        else:
            return False
    return True

def is_ascending(levels):
    pop_count = 0
    new_levels = list(levels)
    for i in range(len(levels)-1):
        if int(levels[i]) < int(levels[i+1]):
            continue
        else:
            if pop_count < 1:
                if i + 2 < len(levels) and int(levels[i]) < int(levels[i + 2]):
                    pop_count += 1
                    new_levels.pop(i)
            # else:
            #     return False
    if pop_count != 0:
        return adjacent_diff(new_levels)
    else:
        return adjacent_diff(levels)
    
    
def is_descending(levels):
    pop_count = 0
    new_levels = list(levels)
    for i in range(len(levels) - 1):
        if int(levels[i]) > int(levels[i + 1]):
            continue
        else:
            if pop_count < 1:
                if i + 2 < len(levels) and int(levels[i]) > int(levels[i + 2]):
                    pop_count += 1
                    new_levels.pop(i)
            # else:
            #     return False
    if pop_count != 0:
        return adjacent_diff(new_levels)
    else:
        return adjacent_diff(levels)


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
    # print(is_ascending(['1', '3', '2', '4', '5']))
    # print(is_descending(['8', '6', '4', '4', '1']))
    # print(adjacent_diff(['1', '3', '2', '4', '5']))
    print(count_safe_reports(input_file))

# ['7', '6', '4', '2', '1'],: Safe without removing any level.
#  ['1', '2', '7', '8', '9'],: Unsafe regardless of which level is removed.
#  ['9', '7', '6', '2', '1'],: Unsafe regardless of which level is removed.
#  ['1', '3', '2', '4', '5'],: Safe by removing the second level, 3.
  #  0    1    2    3    4    len 5
#  ['8', '6', '4', '4', '1'],: Safe by removing the third level, 4.
#  ['1', '3', '6', '7', '9']: Safe without removing any level.