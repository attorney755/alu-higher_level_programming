#!/usr/bin/python3

print("".join(chr(ord('a') + i) if i % 2 == 0 else chr(ord('A') + i) for i in range(25, -1, -1)))
