#!//usr/bin/envZpython3

import sys

file_name = sys.argv[1]
list = sys.argv[2:]
i = 0

with open(file_name, "w") as f:
  while i < len(list):
    message = list[i]
    f.write(message + "\n")
