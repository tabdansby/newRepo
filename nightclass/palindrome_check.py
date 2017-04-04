
p = input("Enter a word to check whether it's a palindrome: ")

if p == p[::-1]:
    print("This is a palindrome!")
else:
    print(p[::-1])
    print(p + " is not a palindrome".format())
