#!/usr/bin/env python3

import argparse

VOWEL_LETTERS = ["a", "e", "i", "o", "u"]
PHRASE = "Ahoy, Captain, {} {} off the larboard bow!"

def main():
    input = getInput()
    alarm = generate_alarm_phrase(input.object)
    print(alarm)

def generate_alarm_phrase(sightedObject):
    if sightedObject == None:
        return ""

    if len(sightedObject) == 0:
        return ""

    startsWithVowel = is_vowel(sightedObject[0])
    if startsWithVowel:
        grammer = "an"
    else:
        grammer = "a"
    phrase = PHRASE.format(grammer, sightedObject)
    return phrase

def is_vowel(letter):
    if letter == None:
        return False

    if len(letter) != 1:
        return False

    if letter.lower() in VOWEL_LETTERS:
        return True

    return False

def getInput():
    parser = createArgsParser()
    args = parser.parse_args()
    return args

def createArgsParser():
    parser = argparse.ArgumentParser(description="Alert on Sighting!")
    parser.add_argument("object", help="What was sighted?")
    return parser

if __name__ == '__main__':
    main()

