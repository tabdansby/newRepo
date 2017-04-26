"""Lab: List Doubles

Goal

Write a function to take a list, and return a new list with each element multiplied by n, excluding elements resulting in zero.

Instructions

Write your function to accept two parameters: the input list and n. Iterate over the list, and using a list building pattern multiplying each element by n. If the product of an element and n is equal to 0, do not include it in the output list.


Documentation

Python Official: Operators - https://docs.python.org/3/library/operator.html
Advanced

Write a solution that employs "python list comprehensions"
Super Advanced

from operator import mul
Use the map() builtin to map the mul() method over your list.
Key Concepts

for looping
Operators
Functions with multiple arguments
Writing doctests"""

#iterating over a list

input_list = [1, 5, 6, 7, 3, 0]
n = 5


def list_doubles(input_list, n):
    new_list = []

    for i in input_list:
        if i*n is not 0:
            new_list.append(i*n)
        else:
            pass
    print(new_list)

list_doubles(input_list, n)



