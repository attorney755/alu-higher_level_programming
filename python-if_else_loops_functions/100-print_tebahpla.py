#!/usr/bin/python3

for i in range(25, -1, -1):
    char = chr(ord('a') + i) if i % 2 == 0 else chr(ord('A') + i)
    print(char, end='')

print()
