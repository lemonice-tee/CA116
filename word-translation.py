#!/usr/bin/env python3

import sys

german = {}
i = 0
with open("translation.txt") as f:
  a = f.readlines()

while i < len(a):
  tokens = a[i].rstrip()
  list = tokens.split()
  german[list[0]] = list[1]
  i = i + 1
i = 0
a = sys.stdin.readlines()
while i < len(a):
  translation = a[i].rstrip()
  if translation in german:
    print(german[translation])
  i = i + 1
