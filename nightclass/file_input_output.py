name = input("What is your name?: ")

with open("hello.txt", "w") as hello:
    hello.write('Hello {}!'.format(name))
    print("Hello " + name)