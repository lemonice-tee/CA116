#!/usr/bin/env python3

smallest = 100

c = 10

i = 0
while i < c:
  n = int(input())
  if n >= 1 and smallest > n:
    smallest = n
  i = i + 1

print(smallest)
