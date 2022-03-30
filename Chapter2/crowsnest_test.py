#!/usr/bin/env python3

import os
import pytest
from subprocess import getstatusoutput, getoutput

from crowsnest import *

VOWEL_WORDS = ["octopus", "iceberg"]
NONVOWEL_WORDS = ["norwhal", "dolphin", "mermaid", "brigantine"]

### ---------------------------------------------------------------------------
###     get_article
### ---------------------------------------------------------------------------

def test__get_article__noneEntered():
    input = None
    expected = "a"
    output = get_article(input)
    assert expected == output

def test__get_article__emptyStringEntered():
    input = ""
    expected = "a"
    output = get_article(input)
    assert expected == output

def test__get_article__lowercase_vowel():
    for word in VOWEL_WORDS:
        expected = "an"
        output = get_article(word.lower())
        assert expected == output

def test__get_article__lowercase_vowel_with_capital_in_middle():
    input = "iPod"
    expected = "an"
    output = get_article(input)
    assert expected == output

def test__get_article__uppercase_vowel():
    for word in VOWEL_WORDS:
        expected = "An"
        output = get_article(word.title())
        assert expected == output

def test__get_article__lowercase_nonvowel():
    for word in NONVOWEL_WORDS:
        expected = "a"
        output = get_article(word.lower())
        assert expected == output

def test__get_article__uppercase_nonvowel():
    for word in NONVOWEL_WORDS:
        expected = "A"
        output = get_article(word.title())
        assert expected == output

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

prg = './Chapter2/crowsnest.py'
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
        assert out.strip() == template.format('A', word.title())


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
        assert out.strip() == template.format('An', word.upper())
