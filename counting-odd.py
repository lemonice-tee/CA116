#!/usr/bin/env python3

n = int(input())

c = 0
i = 1

while c < n:
  if (i % 2 != 0):
    print(i)
    c = c + 1
  i = i + 1
