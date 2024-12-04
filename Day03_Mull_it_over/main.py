#!/usr/bin/env python3
import re

def add_mulls(match_list):
    counter = 0
    for m in match_list:
        mul_result = int(m[0]) * int(m[1])
        # print(mul_result)
        counter +=  mul_result
    return counter


def main():
    input_file = './input.txt'
    MUL_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(input_file, 'r') as f:
        matches = re.findall(MUL_PATTERN, f.read()) # Readlines is a list. DOES NOT WORK. Use read(), it's one
            
    print(add_mulls(matches))


if __name__ == '__main__':
    main()
