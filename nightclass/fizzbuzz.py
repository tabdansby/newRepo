number = int(input('What is the last number of the range?'))

def FizzBuzz(number):

    for num in range(1, number):
        if num%3 == 0 and num%5 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')
        else:
            print(num)

FizzBuzz(number)


#multiples of 3 print Fizz, multiple of 5 print Buzz, multiple of both print FizzBuzz