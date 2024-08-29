#
# Author: ARYAN TUWAR
# Student Number: 112137229
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def linear_search(value, key, index=0):
    if index >= len(value):
        return -1
    if value[index] == key:
        return index
    return linear_search(value, key, index + 1)


def binary_search(value, key, low=0, high=None):
    if high is None:
        high = len(value) - 1
    if low > high:
        return -1

    mid = (low + high) // 2
    if value[mid] == key:
        return mid
    elif value[mid] > key:
        return binary_search(value, key, low, mid - 1)
    else:
        return binary_search(value, key, mid + 1, high)