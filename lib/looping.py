#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while (i >= 0):
        if (i == 0):
            print("Happy New Year!")
        else:
            print(i)
        i-=1
    pass

def square_integers(int_list):
    # code goes here!
    squared = []
    for integer in int_list:
        square = integer * integer
        squared.append(square)
    return squared
    pass

def fizzbuzz():
    # code goes here!
    for n in range(1, 101):
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)
    pass
#happy_new_year()
#print(square_integers([1, 2, 3, 4, 5]))
print(fizzbuzz())