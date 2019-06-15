#!/usr/bin/env python

val1 = 1
val2 = 2
total = 2
newVal = 0
while newVal < 4000000:
    newVal = val1 + val2
    if newVal > 4000000:
        break
    if newVal % 2 == 0:
        total += newVal
    val1 = newVal
    newVal = val1 + val2
    if newVal > 4000000:
        break
    if newVal % 2 == 0:
        total += newVal
    val2 = newVal
print(total)