#!/usr/bin/env python3

import pytest

from apples import *

# ### ---------------------------------------------------------------------------
# ###     transform_message
# ### ---------------------------------------------------------------------------

@pytest.mark.parametrize("input, vowel, expected",[
    ("foo", "a", "faa"),
    ("Apples and Bananas", "i", "Ipplis ind Bininis"),
    ("APPLES AND BANANAS", "i", "IPPLIS IND BININIS"),
    #("Apples and Bananas", "", "Apples and Bananas"),
])
def test__transform_message__uppercase(input, vowel, expected):
  output = transform_message(input, vowel)
  assert expected == output
