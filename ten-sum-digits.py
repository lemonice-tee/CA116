#!/usr/bin/env python3

i = 0
total = 0

while i < 10:
  n = int(input())
  if n < 0:
    small = (n * -1) % 10
  else:
    small = n % 10
  total = total + small
  i = i + 1

print(total)
