#!/usr/bin/env python3

c = 10

i = 0
while i < c:
  n = int(input())
  if i == 0 or largest < n:
    largest = n
  i = i + 1

print(largest)
