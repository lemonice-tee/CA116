#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()

tasks = {}
seenList = []

i = 0

while i < len(s):
   line = s[i].strip().split(".")
   task = line[0] + "." + line[1]
   if task not in tasks:
      tasks[task] = line[2]
      if task not in seenList:
         seenList.append(task)
   elif task in tasks:
      tasks[task] = line[2]
   i = i + 1

i = 0
while i < len(seenList):
   if tasks[seenList[i]] == "correct":
      print(seenList[i])
   i = i + 1
