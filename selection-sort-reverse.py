#!/usr/bin/env python3

a = []
n = input()
while n != "end":
  a.append(int(n))
  n = input()

i = 0
p = 0
smallest = 0
while i < len(a):
  # Find the position p of the smallest element in a from position i to the end
  # Swap the elements at positions i and p
  j = i + 1
  p = i
  while j < len(a):
    if int(a[p]) < int(a[j]):
      p = j
    j = j + 1
  tmp = a[i]
  a[i] = a[p]
  a[p] = tmp
  i = i + 1
x = 0
while x < len(a):
  print(a[x])
  x += 1
