#!/usr/bin/env python3

n = int(input())

i = 1
c = 0

while c < n:
  if (i % 2 == 0):
    print(i)
    c = c + 1
  i = i + 1
