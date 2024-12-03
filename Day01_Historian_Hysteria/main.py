#!/usr/bin/env python3

# TODO: read input list fro file
def load_data(input_file):
    with open(input_file, 'r') as f:
        list_a, list_b = [],[]
        lines = f.readlines()
        for line in lines:
            list_a.append(int(line.split()[0]))
            list_b.append(int(line.split()[1]))

    return list_a, list_b

# TODO: Sort each list from small to big
def sort_lists(list_a, list_b):
    list_a.sort()
    list_b.sort()
    return list_a, list_b


# TODO: Calculate difference between each number on the same index
def calculate_new_diff_list(list_a, list_b):
    diff_list = []
    for i in range(len(list_a)):
        diff_list.append(abs(list_a[i] - list_b[i]))
    return diff_list


# TODO: calculate total distance of the difference list
def calculate_total_distance(diff_list):
    total_distance = 0
    for i in range(len(diff_list)):
        total_distance += diff_list[i]
    return total_distance

# TODO: Calculate similarity between score
def calculate_similarity(list_a, list_b):
    similarity_score = 0
    for i in range(len(list_a)):
        similarity_score += (int(list_a[i] * list_b.count(list_a[i])))
    return similarity_score

if __name__ == '__main__':
    list_a, list_b = load_data('./input.txt')
    list_a, list_b = sort_lists(list_a, list_b)

    diff_list = calculate_new_diff_list(list_a, list_b)

    print(calculate_total_distance(diff_list))

    print(calculate_similarity(list_a, list_b))