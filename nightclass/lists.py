"""lists are iterable and positional. Tuples and sets are in parentheses. Can't
do reassignments to tuples after they are created. They're immutable. If a list is in a tuple,
you can change the items in the list inside the tuple, not the tuple itself."""

x = 5
y = ['the', 42, ['Bye']]

lst = [23, 53, 3, 7, 19]

#print(lst[3][2][0])
#for thing in lst:
#    print(thing)

#print(len(lst))
"""for loop: it will run a function on a given list of items until it stops.
in loops, you can call an item in a list anything. Don't name it the same as a
variable you've already defined. This is called (variable) shadowing, and can
get confusing and possibly break your program

for index in range(len(lst)):
    lst[index]+= 5
    print('index:{}, value: {}'.format(index, lst[index]))"""
