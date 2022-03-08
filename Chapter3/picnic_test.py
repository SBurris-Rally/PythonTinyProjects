#!/usr/bin/env python3

import os
import pytest
from subprocess import getoutput

from picnic import *

### ---------------------------------------------------------------------------
###     displayItems
### ---------------------------------------------------------------------------

@pytest.mark.parametrize("items, useOxfordComma, delimiter, expected",[
    # Use Oxford Comma
    (["apple"], False, ",", "apple"),
    (["apple", "banana"], False, ",", "apple and banana"),
    (["apple", "banana", "cherry"], False, ",", "apple, banana, and cherry"),
    (["apple", "banana", "cherry", "donuts"], False, ",", "apple, banana, cherry, and donuts"),
    # No Oxford Comma (these people are wrong!!!)
    (["apple"], True, ",", "apple"),
    (["apple", "banana"], True, ",", "apple and banana"),
    (["apple", "banana", "cherry"], True, ",", "apple, banana and cherry"),
    (["apple", "banana", "cherry", "donuts"], True, ",", "apple, banana, cherry and donuts"),
    # Change Delimitor
    (["apple"], False, "|", "apple"),
    (["apple", "banana"], False, "|", "apple and banana"),
    (["apple", "banana", "cherry"], False, "|", "apple| banana| and cherry"),
    (["apple", "banana", "cherry", "donuts"], False, "|", "apple| banana| cherry| and donuts"),
    # Delimiter Not Defined
    (["apple", "banana", "cherry"], False, None, "apple, banana, and cherry"),
    (["apple", "banana", "cherry"], False, "", "apple, banana, and cherry"),
    (["apple", "banana", "cherry"], False, " ", "apple, banana, and cherry"),
    (["apple", "banana", "cherry"], False, "  ", "apple, banana, and cherry"),
])
def test_displayItems(items, useOxfordComma, delimiter, expected):
    output = displayItems(items, useOxfordComma, delimiter)
    assert expected == output

### ---------------------------------------------------------------------------
###     processItems
### ---------------------------------------------------------------------------

@pytest.mark.parametrize("items, expected",[
  ("apples", "You are bringing apples."),
])
def test_finalizeSentence(items, expected):
    output = finalizeSentence(items)
    assert expected == output

### ---------------------------------------------------------------------------
###     processItems
### ---------------------------------------------------------------------------

@pytest.mark.parametrize("items, isSorted, expected",[
    (None,True,["<no items>"]),
    (None,False,["<no items>"]),
    ([],True,["<no items>"]),
    ([],False,["<no items>"]),
    (["b"], True, ["b"]),
    (["b"], False, ["b"]),
    (["b", "a"], True, ["a", "b"]),
    (["b", "a"], False, ["b", "a"]),
    (["b", "a", "c"], True, ["a", "b", "c"]),
    (["b", "a", "c"], False, ["b", "a", "c"])
])
def test_proccessItems(items, isSorted, expected):
  output = processItems(items, isSorted)
  assert expected == output
