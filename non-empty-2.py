#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

i = 0
c = 0
while i < len(a) and a[i] == "":
  i = i + 1

if i < len(a):
  print(a[i])

#while i < len(a):
#  if a[i] == "":
#    c = c * 0
#  else:
#     print(a)
#  i = i + 1
