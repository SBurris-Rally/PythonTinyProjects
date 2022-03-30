#!/usr/bin/env python3

import argparse

JUMP_LOOKUP = {
    "0": "5",
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
}

def main():
    input = get_input()
    output = process_message(input)
    print(output)

def process_message(input):
    if input is None:
        return ""

    output = ""
    for letter in input:
        output += transform_character(letter)
    return output

def transform_character(character):
    if character.isnumeric():
        return transform_number(character)
    return character

def transform_number(number):
    if number not in JUMP_LOOKUP:
        return number
    return JUMP_LOOKUP[number]

def get_input():
    parser = create_args_parser()
    args = parser.parse_args()
    return args.text

def create_args_parser():
    parser = argparse.ArgumentParser(description="Jump the Five")
    parser.add_argument("text", metavar='str', help="Input text")
    return parser

if __name__ == '__main__':
    main()