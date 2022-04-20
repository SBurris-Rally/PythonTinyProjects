#!/usr/bin/env python3

import argparse
from calendar import c
import io
import os
import sys
from functools import partial

READ_SIZE = 1000000 # 1 MB at a time

class Input_Values:
  def __init__(self) -> None:
    self.Vowel = "a"
    self.Text = ""

  def process_args(self, args: argparse.Namespace) -> None:
    self.Vowel = args.vowel
    self.Text = args.text

def main():
  input_values = get_input_values()

  input_stream = get_input_stream(input_values)
  output_stream = get_output_stream("output.txt")

  process_data(input_stream, output_stream, input_values)

  input_stream.close()
  output_stream.close()

def process_data(input_stream: io.TextIOWrapper,
                  output_stream: io.TextIOWrapper,
                  input_values: Input_Values
                ) -> None:
  for chunk in iter(partial(input_stream.read, READ_SIZE), ''):
    message = transform_message(chunk, input_values.Vowel)
    output_stream.write(message)

def transform_message(message: str, vowel: str):
  output = []

  output = [
    vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    for c in message
  ]

  return ''.join(output)

def get_output_stream(output_filename = "") -> io.TextIOWrapper:
  no_filename = output_filename.strip() == ""
  if no_filename == True:
    return sys.stdout
  return open(output_filename, "wt")

def get_input_stream(input_values: Input_Values) -> io.TextIOWrapper:
  is_file = os.path.isfile(input_values.Text)
  if is_file == True:
    return open(input_values.Text)
  return io.StringIO(input_values.Text + '\n')

def get_input_values() -> Input_Values:
  parser = create_args_parser()
  args = parser.parse_args()
  input_values = Input_Values()
  input_values.process_args(args)

  return input_values

def create_args_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description="Apples and Bananas", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("text", metavar='text', type=str, help="Input text or file")
  parser.add_argument("-v", "--vowel", metavar="vowel", type=str, default="a", choices=list('aeiou'), help="The vowel(s) allowed")
  return parser

if __name__ == '__main__':
  main()
