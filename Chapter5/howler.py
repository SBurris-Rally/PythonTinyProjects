#!/usr/bin/env python3

import argparse
import os

def main():
    input = get_input()
    message = get_message(input["message"])
    message = process_message(message, input["is_lowercase"])
    output_message(message, input["output_filename"])

def output_message(message, output_filename):
    if output_filename == "":
        print(message)
    else:
        with open(output_filename, "w") as writer:
            writer.write(message)

def process_message(input, is_lowercase):
    if is_lowercase == True:
        return input.casefold()
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
    return {
        "message": args.text,
        "output_filename": args.output,
        "is_lowercase": args.ee
    }


def create_args_parser():
    parser = argparse.ArgumentParser(description="Jump the Five")
    parser.add_argument("text", metavar='str', type=str, help="Input text")
    parser.add_argument("-o", "--output", help="Output filename", metavar="str", type=str, default="")
    parser.add_argument("-ee", metavar='bool', type=bool, default=False, action=argparse.BooleanOptionalAction, help="Write in all lowercase")
    return parser

if __name__ == '__main__':
    main()