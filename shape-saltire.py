#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
  print(((i * " ") + "*") + (" " * (n - i - 3) + "*"))
  i = i + 1
