#!/usr/bin/env python3
import re


def columns_to_lists(grid_data):
    """
    input: grid data in form of list of lists
    returns: list of tuples, columns swapped as rows vice versa
    """
    # [('f', 'b', 'q', 'f'), 
    #  ('o', 'a', 'u', 'a'),
    #  ('o', 'r', 'd', 'r'),
    #  ('b', 'f', 'd', 'l'),
    #  ('a', 'o', 'a', 'o'),
    #  ('r', 'o', 'q', 'c')]
    return [list(column) for column in zip(*grid_data)]


def reverse_list(list_to_revert):
    """
    https://www.geeksforgeeks.org/python-reversing-list/
    ['f', 'o', 'o', 'b', 'a', 'r']
    ['r', 'a', 'b', 'o', 'o', 'f']
    """
    return "".join(list_to_revert[::-1])


def diagonal_left_to_right(grid_data):
    """
    input: matrix data list of lists
    returns: list of lists created from left to right diagonals
    """
    diagonals_all = []
    rows = len(grid_data)
    cols = len(grid_data[0])
    # print (f"rows: {rows} and cols: {cols}")

    # Top top row, left most colum
    for col_y in range(cols):
        diagonal_list = []
        x,y = 0, col_y
        
        # print("list:")
        while x < rows and y < cols:
            diagonal_list.append(grid_data[x][y])
            # print(grid_data[x][y])
            # print(f"x: {x} and y: {y}")
            x += 1
            y += 1

        diagonals_all.append(diagonal_list)

     # 2nd row, left most colum
    for row_x in range(1, rows):
        diagonal_list = []
        x,y = row_x, 0
        
        # print("list:")
        while x < rows and y < cols:
            diagonal_list.append(grid_data[x][y])
            # print(grid_data[x][y])
            # print(f"x: {x} and y: {y}")
            x += 1
            y += 1
        diagonals_all.append(diagonal_list)
    
    return diagonals_all # List of lists


def diagonal_right_to_left(grid_data):
    diagonals_all = []
    rows = len(grid_data)
    cols = len(grid_data[0])
    # print (f"rows: {rows} and cols: {cols}")
    
    # https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards 
    # for i in reversed(range(len(grid_data))):
    #     print(i)


    # Top top row, right most colum
    for col_y in reversed(range(cols)):
        diagonal_list = []
        x,y = 0, col_y
        
        # print("list:")
        while x < rows and y >= 0:
            diagonal_list.append(grid_data[x][y])
            # print(grid_data[x][y])
            # print(f"x: {x} and y: {y}")
            x += 1
            y-= 1
        diagonals_all.append(diagonal_list)

     # 2nd row, right most colum
    for row_x in range(1,rows):
        diagonal_list = []
        x,y = row_x, -1
        
        # print("list:")
        while x < rows and abs(y) < cols:
            diagonal_list.append(grid_data[x][y])
            # print(grid_data[x][y])
            # print(f"x: {x} and y: {y}")
            x += 1
            y -= 1
        diagonals_all.append(diagonal_list)
    
    return diagonals_all # List of lists


def join_list(input_list):
    """
    Takes in a list as input.
    Returns a string
    """
    return "".join(input_list)


def transform_input_to_matrix(input_text_file):
    grid_data = []
    input_f = input_text_file.read().split("\n") # List of items. item is one row of the original text
    # print(input_f)
    for grid in input_f:
        grid_data.append(list(grid))

    return grid_data

def search_for_string(list_data):
    """
    input: list of lists
    output: integer count of matched text
    """
    counter = 0
    search_pattern = "XMAS"
    search_pattern_reversed = "SAMX"

    for row in list_data:
    #   convert list to string
        row_as_string = join_list(row)
    #   search text, update counter if needed, else move on
        matches = re.findall(search_pattern, row_as_string)
        # print(matches)
        for m in matches:
            counter += 1

        reverse_matches = re.findall(search_pattern_reversed, row_as_string)
        # print(reverse_matches)
        for r in reverse_matches:
            counter += 1
    
    return counter

def main():
    input_file = './input.txt'
    # input_file = './input_text_18_occ.txt' 
    matrix_data = []   
    main_count = 0
    with open(input_file, 'r') as f:
        matrix_data = transform_input_to_matrix(f)

    # 1. Search horizontal  function, input list of lists
    main_count += search_for_string(matrix_data)

    # 2. Transform columns to rows, search again
    matrix_data_cols_to_rows = columns_to_lists(matrix_data)
    main_count += search_for_string(matrix_data_cols_to_rows)

    # 3. Create diagonal lists left to right and count
    matrix_data_diagonal_ltr = diagonal_left_to_right(matrix_data)
    main_count += search_for_string(matrix_data_diagonal_ltr)

    # 4. Create diagonal lists right to leftand count
    matrix_data_diagonal_rtl = diagonal_left_to_right(matrix_data)
    main_count += search_for_string(matrix_data_diagonal_rtl)

    print(main_count)

    ## TEST CODE ##
    # lines_of_chars = [
    # ['f', 'o', 'o', 'b', 'a', 'r'], 
    # ['b', 'a', 'r', 'f', 'o', 'o'],
    # ['q', 'u', 'd', 'd', 'a', 'q'], 
    # ['f', 'a', 'r', 'l', 'o', 'c']
    # ]
    # print(reverse_list(['f', 'o', 'o', 'b', 'a', 'r']))
    # print(type(join_list(['f', 'o', 'o', 'b', 'a', 'r'])))
    # search_for_string()
    # print(columns_to_lists(lines_of_chars))
    # print(diagonal_left_to_right(lines_of_chars))
    # print(diagonal_right_to_left(lines_of_chars))


if __name__ == '__main__':
    main()