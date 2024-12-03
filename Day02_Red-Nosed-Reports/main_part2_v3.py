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


def is_asc_or_desc(diff_list):
        positive_count = 0
        negative_count = 0
        for i in range(len(diff_list)):
            if diff_list[i] > 0:
                positive_count += 1
            elif diff_list[i] < 0:
                negative_count += 1
            else:
                continue
        
        if positive_count >= (len(diff_list)-1):
            return 1
        elif negative_count >= (len(diff_list)-1):
            return 0

def get_damper_index(damp_list, asc_ord_desc):
    damp_index = 0
    if asc_ord_desc == 1: # ascending
        for i in range(len(damp_list)):
            if damp_list[i] < 0:
                damp_index = i
                # print("\nfound damp value ascending")
                return damp_index
            else:
                continue
        return None
        
    elif asc_ord_desc == 0: # descending
            for i in range(len(damp_list)):
                if damp_list[i] > 0:
                    damp_index = i
                    # print("\nfound damp value descending")
                    return damp_index
                else:
                    continue
            return None


def abs_gt_one(a,b):
    if abs(b - a) >= 1:
        return True
    return False

def abs_lt_three(a,b):
    if abs(b - a) <= 3:
        return True
    return False

def get_safety_status(safe_levels):
    print(f"\n{safe_levels}")
    for i in range(len(safe_levels)-1):
        a,b = safe_levels[i], safe_levels[i+1]
        
        if abs_gt_one(a,b) and abs_lt_three(a,b):
            print(f"b-a passes")
        else:
            print("b-a DOES NOT PASS")
            return False
    return True
        

def count_safe_reports(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f.readlines():
            levels = line.split() # levels list of strings now
            levels_int = convert_list_to_integer(levels)
            print(f"\nPre processing list: {levels_int}")

            # 1. DIFF List
            diff_list = create_difflist(levels)

            # 2. Get asc or desc
            asc_or_desc = is_asc_or_desc(diff_list)
            print(f"ascending/descending : {asc_or_desc}")

            # CODE WORKS TO RIGHT ABOVE THIS LINE. SOMETHING WRONG WITH FUNCTIONS BELOW
            # 3. Get damper index number
            damper_index = get_damper_index(diff_list, asc_or_desc)
            print(damper_index)
            if damper_index == None:
                if get_safety_status(levels_int):
                    count += 1
                # print("damper is none")

            elif damper_index != 0:
                levels_int.pop(damper_index+1)
                if get_safety_status(levels_int):
                    count += 1
                # print("damper is NOT NONE")

    print(f"\n####\n{count}\n")
            
            # 4. Get adjacent differences from original list
            # if is_safe:
            #     count += 1
        
    # print(count)


                
if __name__ == '__main__':
    input_file = './input.txt'
    count_safe_reports(input_file)