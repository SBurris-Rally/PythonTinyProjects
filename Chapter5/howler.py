#!/usr/bin/env python3

import argparse
import os

def main():
    input = get_input()
    message = get_message(input)
    message = process_message(message)
    print(message)

def process_message(input):
    return input.upper()

def get_message(input):
    is_file = os.path.isfile(input)
    if is_file == True:
        message = get_file_contents(input)
        return message
    else:
        return input

def get_file_contents(filepath):
    try:
        with open(filepath) as reader:
            message_lines = reader.readlines()
            message = " ".join(message_lines)
            return message
    except:
        return ""

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