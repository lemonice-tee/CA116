#!/usr/bin/env python3

import sys

s = sys.stdin.read().split()
i = 0
lines = []

# REMOVE ALL CHARACTERS BEFORE "("  AND AFTER ")"
while i < len(s):
  j = i
  lines = []
  while j < len(s) and i == "(" and j - 1 != ")" :
    lines.append(s[j])
    j += 1
  j += 1
  i = j

print(" ".join(s[i:j]))
