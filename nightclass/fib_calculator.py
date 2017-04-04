#This is a demo of a recursive function

def fib(n):
    print(n)#<-- this print statement takes up much more processing speed/capacity
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)#<-- this function calls itself until it
        #returns a 0 or 1; important thing to remmber: we have to have some way
        #to end the loop. n is the iteration you're starting with. Ex. if n = 40,
        #you're starting at the 40th iteration in the Fibonacci sequence
