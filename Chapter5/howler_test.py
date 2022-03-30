#!/usr/bin/env python3

#LC_ALL=C tr -dc A-Za-z0-9_s < /dev/urandom | head -c 1000000000 > ~/Documents/temp/largefile.txt

import pytest

from howler import *

# ### ---------------------------------------------------------------------------
# ###     transform_message
# ### ---------------------------------------------------------------------------

@pytest.mark.parametrize("input, is_lowercase, expected",[
    ("Hello World", False, "HELLO WORLD"),
    ("Hello World", True, "hello world"),
    ("Hello World!!!", False, "HELLO WORLD!!!"),
    ("Hello World!!!", True, "hello world!!!"),
])

def test__transform_message__uppercase(input, is_lowercase, expected):
    output = transform_message(input, is_lowercase)
    assert expected == output