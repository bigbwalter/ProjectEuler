#!/usr/bin/env python

def checkIfPalindrome(number):
    reverse = 0
    tempNumber = number
    while tempNumber is not 0:
        reverse *= 10
        reverse += tempNumber % 10
        tempNumber = tempNumber // 10
    if reverse == number:
        return True
    return False