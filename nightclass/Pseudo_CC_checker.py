"""# Lab: Pseudo-Credit Card Validation

###### Delivery Method: Doctests

--------------

##### Goal

Write a function which returns whether a string containing a credit card number is valid as a boolean.

Write as many sub-functions as necessary to solve the problem.

--------------------

##### Instructions

1. Slice off the last digit.  That is the **check digit**.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
7. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

```
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. Valid!"""
from functools import reduce
cc = [9, 21, 53, 69, 39, 41, 23, 62, 16, 60, 54, 66, 11, 31]

new_cc = cc[::]


def number_check():
    cc_copy = new_cc[::]
    del cc_copy[13]
    new_cc.append(cc_copy)
    a = (cc_copy[::-1])
    a[0::2] = [i*2 for i in a[0::2]]
    a = [i-9 for i in a if i > 9]
    new_cc.append(a)
    a = str(sum(a))
    new_cc.append(a)
    if cc[13] == a[1]:
        print('Credit card successfully validated!')
    else:
        print('Credit card not valid!')

number_check()
##your_list[::2] = [x*2 for x in your_list[::2]]
    #b = []

"""
data = [1,2,3,4,5,6]
for i,k in zip(data[0::2], data[1::2]):
    print str(i), '+', str(k), '=', str(i+k)"""



