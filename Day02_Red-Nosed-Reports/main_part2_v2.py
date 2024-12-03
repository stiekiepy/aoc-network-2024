#!/usr/bin/env python3

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

# 2. Determine ascending or descending
    """ 
    ascending is returned as 1
    descending is returned as 0
    """
def determine_asc_or_desc(diff_input):
    count_asc = 0
    count_desc = 0
    for i in range(len(diff_input)):
        if diff_input[i] > 0:
            count_asc += 1
        elif diff_input[i] < 0:
            count_desc += 1
        else:
            continue
    
    # print(count_asc)
    # print(count_desc)
    if count_asc >= (len(diff_input)-1):
        return 1
    elif count_desc >= (len(diff_input)-1):
        return 0
    else:
        return None

#3. Use problem damper once
def problem_damper(diff_input, asc_or_desc):
    damper_used = 0
    popped_indx = 0
    new_diff_input = list(diff_input)
    if asc_or_desc == 0: #descending list
        for i in range(len(diff_input)):
            if damper_used <=1:
                if diff_input[i] > 0:
                    damper_used += 1
                    popped_indx = i+1
                    new_diff_input.pop(popped_indx)
                else:
                    continue

            elif damper_used > 1:
                return diff_input, damper_used, None
            
        return new_diff_input, damper_used, popped_indx
            
    elif asc_or_desc == 1: #ascending list
        for i in range(len(diff_input)):
            if damper_used <=1:
                if diff_input[i] < 0:
                    damper_used += 1
                    popped_indx = i+1
                    new_diff_input.pop(popped_indx)

                else:
                    continue

            elif damper_used > 1:
                return diff_input, damper_used, None
        
        return new_diff_input, damper_used, popped_indx
    else:
        return diff_input, 0, 0
                
def is_report_safe(safe_list):
    for i in range(len(safe_list)-1):
        a,b = safe_list[i], safe_list[i+1]
        if 1 <= abs(b-a) <= 3:
            continue
        else:
            return 0
    return 1

def count_safe_reports(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            levels = line.split() # levels list of strings now
            diff_list = create_difflist(levels)
            asc_or_desc_bool = determine_asc_or_desc(diff_list)

            if asc_or_desc_bool == None:
                print("##### ABORT this LOOP ######")
                continue
            else:
                damper_output = problem_damper(diff_list, asc_or_desc_bool)
                damper_used = damper_output[1]
                popped_index = damper_output[2]
                # print(f"damper used: {damper_used}")
                # print(f"poppsed index: {popped_index}")

                if damper_used == 1:
                    popped_list = convert_list_to_integer(levels)
                    popped_list.pop(popped_index)
                    print(f"Damper used: {damper_used}, list is {popped_list}")

                elif damper_used == 0:
                    popped_list = convert_list_to_integer(levels)
                    print(f"Damper used: {damper_used}, list is {popped_list}")

                else:
                    if damper_used > 1:
                        continue
                        
            if is_report_safe(popped_list):
                count += 1
        return count
                
if __name__ == '__main__':
    input_file = './input.txt'
    count_safe_reports(input_file)
    # diff_list = create_difflist([24, 26, 27, 24, 28,30,32,34])
    # diff_list = create_difflist([24, 26, 27, 24, 28,30,29, 32,34])
    # diff_list = create_difflist([24, 26, 27, 28,30,32,34])
    # diff_list = create_difflist([68,67,64,65,63,60])
    # diff_list = create_difflist([68,67,64,65,63,60,61,59])
    # diff_list = create_difflist([68,67,64,64,63,60])
    # print(diff_list)
    # print(determine_asc_or_desc(diff_list))

    # asc_or_desc_bool = determine_asc_or_desc(diff_list)
    
    # if asc_or_desc_bool == None:
    #     print("##### ABORT LOOP ######")
    # else:
    #     damper_output = problem_damper(diff_list, asc_or_desc_bool)
    #     damper_used = damper_output[1]
    #     popped_index = damper_output[2]
    #     print(f"damper used: {damper_used}")
    #     print(f"poppsed index: {popped_index}")

    #     if damper_used == 1:
    #         popped_list = [24, 26, 27, 28,30,32,34]
    #         popped_list.pop(popped_index)
    #         print(popped_list)

    #     elif damper_used == 0:
    #         popped_list = [24, 26, 27, 28,30,32,34]
    #         print(popped_list)
    # print("\n")
    # print(is_report_safe(popped_list))
        # print(is_report_safe(safe_list))
    # damper_list, damper_used = problem_damper(diff_list, )
    # print(damper_list, damper_used)


# ['7', '6', '4', '2', '1'],: Safe without removing any level.
#  ['1', '2', '7', '8', '9'],: Unsafe regardless of which level is removed.
#  ['9', '7', '6', '2', '1'],: Unsafe regardless of which level is removed.
#  ['1', '3', '2', '4', '5'],: Safe by removing the second level, 3.
  #  0    1    2    3    4    len 5
#  ['8', '6', '4', '4', '1'],: Safe by removing the third level, 4.
#  ['1', '3', '6', '7', '9']: Safe without removing any level.