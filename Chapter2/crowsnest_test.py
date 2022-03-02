#!/usr/bin/env python3

import os
import pytest
from subprocess import getstatusoutput, getoutput

from crowsnest import *

VOWEL_WORDS = ["octopus", "iceberg"]
NONVOWEL_WORDS = ["norwhal", "dolphin", "mermaid", "brigantine"]

### ---------------------------------------------------------------------------
###     generate_alarm_phrase
### ---------------------------------------------------------------------------

def test__generate_alarm_phrase__noneEntered():
    input = None
    expected = ""
    output = generate_alarm_phrase(input)
    assert expected == output

def test__generate_alarm_phrase__emptyString():
    input = ""
    expected = ""
    output = generate_alarm_phrase(input)
    assert expected == output

def test__generate_alarm_phrase__vowelWords():
    for sightedObject in VOWEL_WORDS:
        expected = PHRASE.format("an", sightedObject)
        output = generate_alarm_phrase(sightedObject)
        assert expected == output

def test__generate_alarm_phrase__nonVowelWords():
    for sightedObject in NONVOWEL_WORDS:
        expected = PHRASE.format("a", sightedObject)
        output = generate_alarm_phrase(sightedObject)
        assert expected == output

### ---------------------------------------------------------------------------
###     is_vowel
### ---------------------------------------------------------------------------

VOWEL_LETTER_INPUTS = ["a", "e", "i", "o", "u"]
NONVOWEL_LETTER_INPUTS = ["b", "m", "z", "1", "$"]

def test__is_vowelis_vowel__noneEntered():
    input = None
    expected = False
    output = is_vowel(input)
    assert expected == output

def test__is_vowel__noLetter():
    input = ""
    expected = False
    output = is_vowel(input)
    assert expected == output

def test__is_vowel__moreThanOneLetter():
    input = "abc"
    expected = False
    output = is_vowel(input)
    assert expected == output

def test__is_vowel__vowelLetters():
    expected = True
    for letter in VOWEL_LETTER_INPUTS:
        output = is_vowel(letter)
        assert expected == output

def test__is_vowel__nonVowelLetters():
    expected = False
    for letter in NONVOWEL_LETTER_INPUTS:
        output = is_vowel(letter)
        assert expected == output



### ---------------------------------------------------------------------------
###     Copied from example
### ---------------------------------------------------------------------------


prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        print(out)
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('an', word.upper())
