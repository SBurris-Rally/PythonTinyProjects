#!/usr/bin/env python3

import argparse

def main():
    print("Hello World")

def createArgsParser():
  parser = argparse.ArgumentParser(description="Alert on Sighting!")
  parser.add_argument("object", help="What was sighted?")
  return parser

if __name__ == "__main__":
    main()
