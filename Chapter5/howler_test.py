#!/usr/bin/env python3

import pytest

from howler import *

# ### ---------------------------------------------------------------------------
# ###     process_message
# ### ---------------------------------------------------------------------------

# @pytest.mark.parametrize("input, expected",[
#     (None, ""),
#     ("", ""),
#     ("Hello World", "Hello World"),
#     ("1", "9"),
#     ("Call 1-800-329-8044 today!", "Call 9-255-781-2566 today!")
# ])
# def test__process_message__normal(input, expected):
#     output = process_message(input)
#     assert expected == output