#!/usr/bin/env python3

s = []
n = input()
i = 0
while n != "end":
  s.append(n)
  n = input()

i = 0
smallest = 0
while i < len(s):
  if int(s[i]) < int(s[smallest]):
    smallest = i
  i = i + 1
print(s[smallest])
