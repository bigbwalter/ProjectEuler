#!/usr/bin/env python

from MathFunctions import checkIfPalindrome

i = 999
result = 0
biggest = 0
while i > 0:
    j = 999
    while j > 0:
        found = checkIfPalindrome(i*j)
        if found:
            result = i*j
            if result > biggest:
                biggest = result
        j -= 1
    i -= 1
print(biggest)