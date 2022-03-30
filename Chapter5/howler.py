#!/usr/bin/env python3

import argparse
import io
import os
import sys
from functools import partial

LARGE_FILE_CUTOFF = 10485760  # 10 MB
READ_SIZE = 1000000 # 1 MB at a time

def main():
    input = get_input()

    message = input["message"]
    is_lowercase = input["is_lowercase"]
    output_filename = input["output_filename"]

    with get_input_stream(message) as input_stream, \
            get_output_stream(output_filename) as output_stream:
        input_stream = get_input_stream(message)
        output_stream = get_output_stream(output_filename)
        process_data(input_stream, output_stream, is_lowercase)

def get_input_stream(input):
    is_file = os.path.isfile(input)
    if is_file == True:
        return open(input)
    return io.StringIO(input + '\n')

def get_output_stream(output_filename):
    no_filename = output_filename.strip() == ""
    if no_filename == True:
        return sys.stdout
    return open(output_filename, "wt")

def process_data(input, output, is_lowercase):
    for chunk in iter(partial(input.read, READ_SIZE), ''):
        message = transform_message(chunk, is_lowercase)
        output.write(message)

def transform_message(message, is_lowercase):
    if is_lowercase == True:
        return message.casefold()
    return message.upper()

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
    parser.add_argument("-ee", action="store_true", help="Write in all lowercase")
    return parser

if __name__ == '__main__':
    main()