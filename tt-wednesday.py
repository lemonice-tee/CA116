#!/usr/bin/env python3

lines = input()
while lines != "end":
  line = lines.split()
  if line[0] == "3":
    line = " ".join(line)
    print(line)
  lines = input()
