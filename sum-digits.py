#!/usr/bin/env python3

n = int(input())
i = 0
total = 0

print((n // 1000) + (n %10 // 100) + (n % 100 // 10) + (n % 1000 // 1))
