#!/usr/bin/env python3
import numpy as np

def columns_to_lists(grid_data):
    """
    Use numpy transpose to get columns as rows.
    """
    return grid_data.T  # Transpose of the matrix


def diagonal_left_to_right(grid_data):
    """
    Extract all diagonals from top-left to bottom-right.
    """
    diagonals = [grid_data.diagonal(offset) for offset in range(-grid_data.shape[0] + 1, grid_data.shape[1])]
    return [list(diagonal) for diagonal in diagonals if len(diagonal) >= 4]

def diagonal_right_to_left(grid_data):
    """
    Extract all diagonals from top-right to bottom-left.
    """
    flipped_grid = np.fliplr(grid_data)  # Flip the matrix horizontally
    diagonals = [flipped_grid.diagonal(offset) for offset in range(-flipped_grid.shape[0] + 1, flipped_grid.shape[1])]
    return [list(diagonal) for diagonal in diagonals if len(diagonal) >= 4]
 

def transform_input_to_matrix(input_text_file):
    """
    Transform input text file into a numpy array.
    """
    grid_data = np.array([list(line.strip()) for line in input_text_file])
    return grid_data

    return grid_data

def search_for_string(grid_data, word, reverse_word):
    """
    Search for occurrences of word and its reverse in numpy array.
    """
    count = 0
    for line in grid_data:
        line_str = ''.join(line)
        count += line_str.count(word)
        count += line_str.count(reverse_word)
    return count

    
    return counter

def main():
    input_file = './input.txt'
    with open(input_file, 'r') as f:
        matrix_data = transform_input_to_matrix(f)

    main_count = 0
    word, reverse_word = "XMAS", "SAMX"

    # Horizontal
    main_count += search_for_string(matrix_data, word, reverse_word)

    # Vertical
    main_count += search_for_string(columns_to_lists(matrix_data), word, reverse_word)

    # Diagonal (Left-to-Right)
    main_count += search_for_string(diagonal_left_to_right(matrix_data), word, reverse_word)

    # Diagonal (Right-to-Left)
    main_count += search_for_string(diagonal_right_to_left(matrix_data), word, reverse_word)

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