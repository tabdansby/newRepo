"""Dictionaries use curly brackets, are mutable like lists; a key has to be an integer
or string, not a list or object   """

a{'inv': {}}
#a = {'key' : [1, 2, 3]}
inp = input("enter something")
a[inp] = "we just added a key called {}".format(inp)
print(a)

#if you try to call a key that isn't in the dictionary, you get an error
