#iterate over a list using list comprehension
input_list = [1, 5, 6, 7, 3, 0]
n = 5
new_list = []

def list_doubles(input_list, n):

    list_comp = [num*n for num in input_list if num != 0]:
        new_list.append(list_comp)


print(new_list)



