#!/usr/bin/env python3

import sys
n = int(sys.argv[1])
i = 0
m = n ** (0.5)

while i <= m:
  if n ** (0.5) > i:
    print(i)
  i += 1
  #  #  WHEN NUMBER + X OVER THE CLOSEST M ^ 2
  #  CONSIDER THAT NEEDED N^
  # WHEN
#while i < n:
#  if n ** (1 / 2) % 2 == 0 or n ** (1 / 2) % 2 == 1:
#    m = n ** (1 / 2)

#print(m)
