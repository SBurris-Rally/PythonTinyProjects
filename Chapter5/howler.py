#!/usr/bin/env python3

import argparse
import os
from functools import partial

LARGE_FILE_CUTOFF = 10485760  # 10 MB
READ_SIZE = 1000000 # 1 MB at a time

def main():
    input = get_input()

    message = input["message"]
    is_lowercase = input["is_lowercase"]
    output_filename = input["output_filename"]

    is_large = is_large_file(message)
    if is_large == False:
        message = get_message(message)
        message = process_message(message, is_lowercase)
        output_message(message, output_filename)
    else:
        process_large_file(message, is_lowercase, output_filename)

def process_large_file(filename, is_lowercase, output_filename):
    index = 0
    with open(filename) as reader:
        for chunk in iter(partial(reader.read, READ_SIZE), b''):
            message = process_message(chunk, is_lowercase)
            print(message)

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

def is_large_file(input):
    is_file = is_message_filename(input)
    if is_file == False:
        return False

    file_size = os.path.getsize(input)
    if file_size > LARGE_FILE_CUTOFF:
        return True
    return False

def is_message_filename(input):
    is_file = os.path.isfile(input)
    return is_file

def get_message(input):
    is_file = is_message_filename(input)
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