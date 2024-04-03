#!/usr/bin/env python3

lines = input()
i = 0

while lines != "end":
  line = lines.split()
  line = " ".join(line[5:])
  print(line)
  lines = input()
