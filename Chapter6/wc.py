#!/usr/bin/env python3

import argparse
import re
import sys
from functools import partial

READ_SIZE = 1000000  # 1 MB at a time


def main():
    files, display_options = get_input()
    results = process_files(files)
    output = format_results(results, display_options)

    for line in output:
        print(line)


def format_results(results, display_options):
    total = File_counts("total")
    output = []
    for result in results:
        total.add(result)
        formated_message = format_single_result(result, display_options)
        output.append(formated_message)

    if len(results) > 1:
        total_message = format_single_result(total, display_options)
        output.append(total_message)

    return output


def format_single_result(result, display_options):
    pattern_fragment = "{:8} "

    output = ""
    if display_options.show_line_count == True:
        output += pattern_fragment.format(result.lines)

    if display_options.show_word_count == True:
        output += pattern_fragment.format(result.words)

    if display_options.show_byte_count == True:
        output += pattern_fragment.format(result.bytes)

    output += result.name

    return output


def process_files(files):
    results = []
    for file_handle in files:
        result = process_file(file_handle)
        results.append(result)

    return results


def process_file(file_handle, read_size=READ_SIZE):
    results = File_counts(file_handle.name)
    was_ending_space = False

    # The author wanted to read one line at a time because he was worried about
    # large files.  A large file can be made up of a single line, so to make extra sure
    # we are not using too much memory at one time, we will read chunks at a time.
    # Optionally: A max file size could be specified and checked before we reached this point.
    for chunk in iter(partial(file_handle.read, read_size), ""):
        results.bytes += len(chunk)
        results.lines += chunk.count("\n")
        chunk = re.sub("[ ]+", " ", chunk)
        results.words += chunk.count(" ")
        
        is_beginning_space = chunk[0] == " "

        # If chunk is split on space, don't double count it
        if is_beginning_space and was_ending_space:
            results.words -= 1
        was_ending_space = chunk[-1] == " "

    if results.bytes > 0 and results.lines != results.bytes:
        results.words += 1

    return results


def get_input():
    parser = create_args_parser()
    args = parser.parse_args()
    files = args.file

    display_options = Display_options(args.lines, args.words, args.characters)

    return files, display_options


def create_args_parser():
    parser = argparse.ArgumentParser(description="Word Count")
    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file(s)",
    )
    parser.add_argument(
        "-l", "--lines", default=False, action="store_true", help="Display line count"
    )
    parser.add_argument(
        "-w", "--words", default=False, action="store_true", help="Display word count"
    )
    parser.add_argument(
        "-c",
        "--characters",
        default=False,
        action="store_true",
        help="Display characters count",
    )
    return parser


class Display_options:
    def __init__(self, show_lines, show_words, show_bytes):
        if show_lines == False and show_words == False and show_bytes == False:
            # If none are specified, display all
            self.show_line_count = True
            self.show_word_count = True
            self.show_byte_count = True
        else:
            self.show_line_count = show_lines
            self.show_word_count = show_words
            self.show_byte_count = show_bytes


class File_counts:
    def __init__(self, file_name):
        self.name = file_name
        self.lines = 0
        self.words = 0
        self.bytes = 0

    def add(self, results):
        self.lines += results.lines
        self.words += results.words
        self.bytes += results.bytes


if __name__ == "__main__":
    main()
