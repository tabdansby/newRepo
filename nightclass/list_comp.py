one = [2, 1, 2, 3, 4]

print([1 - 2 % 2 for n in one])

list_for = []

for n in one:
    y= 1 - n % 2
    list_for.append(y)

print(list_comp)
print(list_for)

"""list comprehension anatomy:
declare a variable and say what it's doing. have to reference it bfore you can assign it:
[x*10 for x in one] meaning for each item in list one, multiply it by 10"""
