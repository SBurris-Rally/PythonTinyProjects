#!/usr/bin/env python3

#LC_ALL=C tr -dc A-Za-z0-9_s < /dev/urandom | head -c 1000000000 > ~/Documents/temp/largefile.txt

import pytest

from gashlycrumb import *

# ### ---------------------------------------------------------------------------
# ###     create_lookup_chart
# ### ---------------------------------------------------------------------------

def test__create_lookup_chart__all_valid_entries():
  input_lines = [
    "A is for Amy who fell down the stairs.",
    "B is for Basil assaulted by bears.",
    "C is for Clara who wasted away."
  ]

  expected = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "B is for Basil assaulted by bears.",
    "C": "C is for Clara who wasted away."
  }

  output = create_lookup_chart(input_lines)

  assert expected == output

def test__create_lookup_chart__different_cased_first_letters():
  input_lines = [
    "A is for Amy who fell down the stairs.",
    "b is for Basil assaulted by bears.",
    "c is for Clara who wasted away."
  ]

  expected = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "b is for Basil assaulted by bears.",
    "C": "c is for Clara who wasted away."
  }

  output = create_lookup_chart(input_lines)

  assert expected == output

def test__create_lookup_chart__use_last_line_if_mulitple_same_letters():
  input_lines = [
    "A is for Amy who fell down the stairs.",
    "a is for Basil assaulted by bears.",
    "a is for Clara who wasted away."
  ]

  expected = {
    "A": "a is for Clara who wasted away.",
  }

  output = create_lookup_chart(input_lines)

  assert expected == output

def test__create_lookup_chart__ignore_lines_that_don_not_start_with_letters():
  input_lines = [
    "A is for Amy who fell down the stairs.",
    "1 is for Basil assaulted by bears.",
    " C is for Clara who wasted away."
    "$ is for Clara who wasted away.",

  ]

  expected = {
    "A": "A is for Amy who fell down the stairs.",
  }

  output = create_lookup_chart(input_lines)

  assert expected == output

# ### ---------------------------------------------------------------------------
# ###     get_matching_lines
# ### ---------------------------------------------------------------------------

def test__get_matching_lines__single_uppercase_letter():
  lookup_chart = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "B is for Basil assaulted by bears.",
    "C": "C is for Clara who wasted away."
  }
  input_values = Input_Values()
  input_values.Letters = ["B"]
  expected = ["B is for Basil assaulted by bears."]

  output = get_matching_lines(input_values, lookup_chart)

  assert expected == output

def test__get_matching_lines__multiple_uppercase_letters():
  lookup_chart = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "B is for Basil assaulted by bears.",
    "C": "C is for Clara who wasted away."
  }
  input_values = Input_Values()
  input_values.Letters = ["B", "A"]
  expected = [
    "B is for Basil assaulted by bears.",
    "A is for Amy who fell down the stairs."
  ]

  output = get_matching_lines(input_values, lookup_chart)

  assert expected == output

def test__get_matching_lines__multiple_mixed_case_letters():
  lookup_chart = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "B is for Basil assaulted by bears.",
    "C": "C is for Clara who wasted away."
  }
  input_values = Input_Values()
  input_values.Letters = ["B", "a"]
  expected = [
    "B is for Basil assaulted by bears.",
    "A is for Amy who fell down the stairs."
  ]

  output = get_matching_lines(input_values, lookup_chart)

  assert expected == output

def test__get_matching_lines__single_letter_not_in_lookup():
  lookup_chart = {
    "A": "A is for Amy who fell down the stairs.",
    "B": "B is for Basil assaulted by bears.",
    "C": "C is for Clara who wasted away."
  }
  input_values = Input_Values()
  input_values.Letters = ["D"]
  expected = [
    "I do not know \"D\"."
  ]

  output = get_matching_lines(input_values, lookup_chart)

  assert expected == output
