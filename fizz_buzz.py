
# This codes takes in a number  and returns the numbers of its range with the numbers divisible by 3 being replaced
# with Fizz and the numbers divisible by 5 being replaced with Buzz.
# The numbers divisible by both are replaced with FizzBuzz.


def fizz(a):
    try:
        for i in range(int(a)+1):
            if i % 3 == 0 and i % 5 != 0:
                print("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            else:
                print(i)
    except ValueError:
        print("you did not enter a number !!")


x = input("Enter a number :  ")
fizz(x)
