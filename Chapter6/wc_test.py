#!/usr/bin/env python3

from cmath import exp
import pytest

from wc import *

# ### ---------------------------------------------------------------------------
# ###     File_counts - add
# ### ---------------------------------------------------------------------------


def test__File_counts__add__normal():
    totals = File_counts("total")
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    expected = helper_create_file_count("total", 1, 2, 3)

    totals.add(first_file)

    helper_are_equal(expected, totals)


# ### ---------------------------------------------------------------------------
# ###     format_results
# ### ---------------------------------------------------------------------------


def test__format_results__single_file_display_all():
    results = []
    display_options = Display_options(True, True, True)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       1        2        3 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_lines_only():
    results = []
    display_options = Display_options(True, False, False)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       1 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_words_only():
    results = []
    display_options = Display_options(False, True, False)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       2 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_bytes_only():
    results = []
    display_options = Display_options(False, False, True)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       3 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_no_lines():
    results = []
    display_options = Display_options(False, True, True)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       2        3 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_no_words():
    results = []
    display_options = Display_options(True, False, True)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       1        3 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__single_file_display_no_bytes():
    results = []
    display_options = Display_options(True, True, False)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    results.append(first_file)
    expected = ["       1        2 foo.txt"]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__two_files_display_all():
    results = []
    display_options = Display_options(False, False, False)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    second_file = helper_create_file_count("bar.txt", 12345678, 12345678, 12345678)
    results.append(first_file)
    results.append(second_file)
    expected = [
        "       1        2        3 foo.txt",
        "12345678 12345678 12345678 bar.txt",
        "12345679 12345680 12345681 total",
    ]

    output = format_results(results, display_options)

    assert expected == output


def test__format_results__two_files_display_lines_only():
    results = []
    display_options = Display_options(True, False, False)
    first_file = helper_create_file_count("foo.txt", 1, 2, 3)
    second_file = helper_create_file_count("bar.txt", 12345678, 12345678, 12345678)
    results.append(first_file)
    results.append(second_file)
    expected = ["       1 foo.txt", "12345678 bar.txt", "12345679 total"]

    output = format_results(results, display_options)

    assert expected == output


# ### ---------------------------------------------------------------------------
# ###     format_single_result
# ### ---------------------------------------------------------------------------


def test__format_single_result__normal():
    display_options = Display_options(True, True, True)
    results = helper_create_file_count("foo.txt", 1, 2, 3)
    expected = "       1        2        3 foo.txt"

    output = format_single_result(results, display_options)

    assert expected == output


def test__format_single_result__eight_digit_numbers():
    display_options = Display_options(True, True, True)
    results = helper_create_file_count("foo.txt", 12345678, 12345678, 12345678)
    expected = "12345678 12345678 12345678 foo.txt"

    output = format_single_result(results, display_options)

    assert expected == output


# ### ---------------------------------------------------------------------------
# ###     process_file
# ### ---------------------------------------------------------------------------


def test__process_file__simple_fox_file():
    filename = "Chapter6/data/fox.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 1, 9, 45)
        output = process_file(input_file)
    helper_are_equal(expected, output)


def test__process_file__empty_file():
    filename = "Chapter6/data/empty.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 0, 0, 0)
        output = process_file(input_file)
    helper_are_equal(expected, output)


def test__process_file__single_blank_line():
    filename = "Chapter6/data/blank_line.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 1, 0, 1)
        output = process_file(input_file)
    helper_are_equal(expected, output)


def test__process_file__two_words_double_space():
    filename = "Chapter6/data/double_space.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 1, 2, 13)
        output = process_file(input_file)
    helper_are_equal(expected, output)


def test__process_file__two_words_double_space_split_chunk_in_space():
    filename = "Chapter6/data/double_space.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 1, 2, 13)
        output = process_file(input_file, 6)
    helper_are_equal(expected, output)


def test__process_file__words_split_across_multiple_chunks():
    filename = "Chapter6/data/double_space.txt"
    with open(filename, "r") as input_file:
        expected = helper_create_file_count(input_file.name, 1, 2, 13)
        output = process_file(input_file, 1)
    helper_are_equal(expected, output)


# ### ---------------------------------------------------------------------------
# ###     Test Helper Functions
# ### ---------------------------------------------------------------------------


def helper_create_file_count(name, lines, words, bytes):
    data = File_counts(name)
    data.lines = lines
    data.words = words
    data.bytes = bytes
    return data


def helper_are_equal(expected, output):
    assert expected.name == output.name
    assert expected.bytes == output.bytes
    assert expected.lines == output.lines
    assert expected.words == output.words
