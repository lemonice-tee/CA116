#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
fruits = {
  "apple": True,
  "banana": True,
  "cherry": True,
  "orange": True,
  "pear": True,
}

i = 0
while i < len(words):
  if words[i].rstrip() in fruits:
    print(words[i].rstrip())
  i = i + 1
