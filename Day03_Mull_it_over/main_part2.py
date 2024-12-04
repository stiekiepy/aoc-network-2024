#!/usr/bin/env python3
import re

def add_mulls(mull_obj):
    counter = 0
    # print(type(mull_obj))
    mul_result = int(mull_obj[0]) * int(mull_obj[1])
    counter +=  mul_result
    return counter


def main():
    input_file = './input.txt'
    # regex helper: https://regex-generator.olafneumann.org/
    MUL_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    DO_PATTERN = re.compile(r"do\(\)")
    DONOT_PATTERN = re.compile(r"don't\(\)")

    with open(input_file, 'r') as f:
        counter = 0
        mul_enabled = True
        # matches = re.findall(MUL_PATTERN, f.read()) # Readlines is a list. DOES NOT WORK. Use read(), it's one
        # Fucking hell: use https://docs.python.org/3/library/re.html#re.finditer

        for match in re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", f.read() ):
            matched_on_text = match.group(0)
            # print(matched_on_text)
            temp_count = 0

            if DO_PATTERN.match(matched_on_text):
                mul_enabled = True
            elif DONOT_PATTERN.match(matched_on_text):
                mul_enabled = False
            elif mul_enabled:  # Only process mul(x, y) if mul is enabled
                mul_obj = MUL_PATTERN.match(matched_on_text).groups()
                # print(mul_obj)
                temp_count = add_mulls(mul_obj)
                # print(temp_count)

            counter += temp_count

        print(counter)


if __name__ == '__main__':
    main()
