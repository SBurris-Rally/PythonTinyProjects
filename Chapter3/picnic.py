#!/usr/bin/env python3

import argparse

PICNIC_TEMPLATE = "You are bringing {}."

def main():
    input = processArguments()
    items = processItems(input.items, input.sorted)
    display_items = displayItems(items, input.no_oxford, input.delimiter)
    finalStatement = finalizeSentence(display_items)
    print(finalStatement)

def finalizeSentence(items):
    return PICNIC_TEMPLATE.format(items)

def displayItems(items, noOxfordComma, delimiter):
    if delimiter is None or delimiter.strip() == "":
        delimiter = ","

    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        if noOxfordComma == False:
            items[-1] = f"and {items[-1]}"
            return f"{delimiter} ".join(items)
        else:
            items[-2] = f"{items[-2]} and {items[-1]}"
            items = items[:-1]
            return f"{delimiter} ".join(items)

def processItems(items, is_sorted):
    if items is None or len(items) == 0:
        return ["<no items>"]

    if is_sorted == True:
        items.sort()
        return items
    return items

def processArguments():
    parser = createArgsParser()
    return parser.parse_args()

def createArgsParser():
    parser = argparse.ArgumentParser(description="Picnic game", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("items", nargs='+', help="What to bring")
    parser.add_argument("-s", "--sorted", default=False, action="store_true", help="Sort the items")
    parser.add_argument("-n", "--no-oxford", action=argparse.BooleanOptionalAction)
    parser.add_argument("-d", "--delimiter", default=",", help="Define list delimiter")
    parser.set_defaults(no_oxford=False)
    return parser

if __name__ == "__main__":
    main()
