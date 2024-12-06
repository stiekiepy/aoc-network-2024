#!/usr/bin/env python3

# Still doesn't work. FML


def convert_list_to_integer(input):
    new_list = list(map(int, input))
    return new_list

# 1. Create a diff list to see if it's ascending or descending
def create_difflist(input_list):
    int_list = convert_list_to_integer(input_list)
    diffs_list = []

    for indx in range(len(int_list)-1):
        a,b = int_list[indx], int_list[indx+1]
        diffs_list.append(b-a)
    return diffs_list

# 2. check if non-zero
def check_non_zero(diff_list):
    for diff in diff_list:
        if diff == 0:
            return False
    return True


# 3. is increasing or decreasing
def is_increasing(diff_list):
    for i in range(len(diff_list)-1):
        a,b = diff_list[i], diff_list[i+1]
        if b > a:
            continue
        else:
            return False
    return True

def is_decreasing(diff_list):
    for i in range(len(diff_list)-1):
        a,b = diff_list[i], diff_list[i+1]
        if b < a:
            continue
        else:
            return False
    return True


# 3a. Helper for 3, slicing lists
def check_splices(items):
    out = []
    # print(items)
    for i in range(len(items)):
        inner = []
        for j in range(len(items)):
            if j != i:
                inner.append(items[j])
        # print(f"Inner is {inner}")
        if is_increasing(inner) or is_decreasing(inner):
            return True
        
    return False

# 4. check adjacent items to be 1 <= item <= 3
def check_adjacent_limit(diff_list):
    for i in range(len(diff_list)-1):
        a,b = diff_list[i], diff_list[i+1]
        if  abs(b-a) <= 3 and abs(b-1) >= 1:
            continue
        else:
            return False
    return True

def count_safe_reports(input_file):
    
    count = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            levels = line.split() # levels list of strings now
            levels_int = convert_list_to_integer(levels)
            # print(f"\nPre processing list: {levels_int}")

            # 1. DIFF List
            diff_list = create_difflist(levels)
            # print(f"\nDiff list is: {diff_list}")

            # 2. Check all non-zero in difflist
            # is_non_zero = check_non_zero(diff_list)
            # is_non_zero = check_non_zero([2,3,-2,4,1])
            # print(f"Is non zero: {is_non_zero}")

            # 3. is increasing or decreasing
            # print(f"Is asc or desc : {check_splices(levels_int)}")

            # 4. check if adj differences is within 1 and 3
            # print(f"Check adj levels pass or not: {check_adjacent_limit(levels_int)}")
            # print(f"Check passes for 1 and 3 range: {check_adjacent_limit(levels_int)}")

            if check_non_zero(diff_list) and check_splices(levels_int) and check_adjacent_limit(levels_int):
                count += 1
    print(count)

# assert is_safe_report([7, 6, 4, 2, 1]) == 42, "Safe because the levels are all decreasing by 1 or 2."
# assert is_safe_report([1, 2, 7, 8, 9]) == False, "Unsafe because 2 7 is an increase of 5."
# assert is_safe_report([9, 7, 6, 2, 1]) == False, "Unsafe because 6 2 is a decrease of 4."
# assert is_safe_report([1, 3, 2, 4, 5]) == False, "Unsafe because 1 3 is increasing but 3 2 is decreasing."
# assert is_safe_report([8, 6, 4, 4, 1]) == False, "Unsafe because 4 4 is neither an increase or a decrease."

# assert is_safe_report([1, 3, 6, 7, 9]) == True, "Safe because the levels are all increasing by 1, 2, or 3."
        
if __name__ == '__main__':
    input_file = './input.txt'
    count_safe_reports(input_file)