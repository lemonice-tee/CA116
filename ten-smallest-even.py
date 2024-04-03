#!/usr/bin/env python3

# base case to compare
smallest = int(input())

i = 0
while i < 9:
  n = int(input())
  if (n % 2 == 0) and smallest > n:
    smallest = n
  i = i + 1

print(smallest)
