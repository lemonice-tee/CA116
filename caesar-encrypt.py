#!/usr/bin/env python3

import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
higher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translations = {}
src = lower + higher
dst = lower[n:] + lower[:n] + higher[n:] + higher[:n]

i = 0
while i < len(src):
  translations[src[i]] = dst[i]
  i = i + 1

a = sys.stdin.read()
s = []
i = 0
while i < len(a):
  if a[i] in translations:
    s.append(translations[a[i]])
  else:
    s.append(a[i])
  i = i + 1

sys.stdout.write("".join(s))
