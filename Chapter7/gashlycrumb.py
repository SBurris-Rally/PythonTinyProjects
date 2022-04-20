#!/usr/bin/env python3

import argparse
from io import TextIOWrapper
from typing import List, Dict

DEFAULT_FILE = "Chapter7/input/gashlycrumb.txt"
UNKNOWN_LETTER_PATTERN = "I do not know \"{}\"."

class Input_Values:
  """Hold all the argument inputs in a strongly typed class"""
  def __init__(self) -> None:
    """Default constructor"""
    self.Letters = []
    self.File = DEFAULT_FILE

  def process_args(self, args: argparse.Namespace) -> None:
    """Pull the arguments from the user into a structured file."""
    self.Letters = list(args.letter)
    self.File = args.file

def main():
  """"""
  input_values = get_input_values()
  lookup = get_lookup_chart(input_values)
  output = get_matching_lines(input_values, lookup)
  display_output(output)

def display_output(output: List[str]) -> None:
  """Output the results to the user."""
  for line in output:
    print(line)

def get_matching_lines(input_values: Input_Values, lookup: Dict[str, str]) -> List[str]:
  """Get the lines from the input file that match the letters the user wants"""
  results = []
  for letter in input_values.Letters:
    letter = letter.upper()

    if letter in lookup:
      selected = lookup[letter]
    else:
      selected = UNKNOWN_LETTER_PATTERN.format(letter)
    results.append(selected)

  return results

def get_lookup_chart(input_values: Input_Values) -> Dict[str, str]:
  """Creates the lookup chart based on the file specified by the user"""
  file_contents = get_file_contents(input_values.File)
  lookup_chart = create_lookup_chart(file_contents)
  return lookup_chart

def get_file_contents(file: TextIOWrapper) -> List[str]:
  """Get all lines from the stream"""
  lines = file.readlines()
  return lines

def create_lookup_chart(content: List[str]) -> Dict[str, str]:
  """Create lookup chart based on the text file defined in the input"""
  lookup_chart = {}

  for line in content:
    letter = line[0].upper()
    if letter.isalpha():
      lookup_chart[letter] = line

  return lookup_chart

def get_input_values() -> Input_Values:
  """Get the CLI arguments passed for this execution run"""
  parser = create_args_parser()
  args = parser.parse_args()
  input_values = Input_Values()
  input_values.process_args(args)

  return input_values

def create_args_parser() -> argparse.ArgumentParser:
  """Define CLI arguments for this program"""
  parser = argparse.ArgumentParser(description="Gashlycrumb", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("letter", metavar='letter', type=str, nargs="+", help="Letters(s)")
  parser.add_argument("-f", "--file", metavar="FILE", type=argparse.FileType('rt'), default=DEFAULT_FILE, help="Input File")
  return parser

if __name__ == '__main__':
  main()
