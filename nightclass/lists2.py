"""lst = [32, 'hi']

num = int(input('What is your favorite number?: '))

lst.append(num)
removed = lst.pop()
print(lst)
.append adds items to the end of a list. .pop deletes things from a list and returns it in the
printed answer. You can reference by index with .pop, but not .append"""

greeting = []

name1 = input('Tell me the name of the first person: ')
name2 = input('Tell me the name of the second person: ')
name3 = input('Tell me the name of the third person: ')

greeting.append(name1)
greeting.append(name2)
greeting.append(name3)

for person in greeting:
    print('Hello {} how are you?'.format(person))
"""using .format, be sure to use the item name (the word after for) in the parentheses
after .format"""
