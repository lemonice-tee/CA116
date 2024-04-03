#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

i = 0
c = 0
while i < len(a):
  if a[i] == "":
    c = c + 0
  else:
    c = c + 1
  i = i + 1

print(c)
