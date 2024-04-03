#!/usr/bin/env python3

import sys
translations = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn",
}


a = sys.stdin.readlines()
i = 0
while i < len(a):
  if a[i].rstrip() in translations:
    print(translations[a[i].rstrip()])
  i = i + 1
