#!/usr/bin/env python 3

n = int(input())

i = 1
c = 0

while c < n:
  if (n % 2 == 0):
    print(n // 2)
    c = c + 1
  else: (n % 2 != 0)
    print((3 * n) + 1)
    c = c + 1
  i = i + 1
