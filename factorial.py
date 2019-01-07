
# The following codes takes in a number and returns its factorial.
# For example 5! = 120.


def factorial(a):
    try:
        if int(a) == 1:
            return 1
        else:
            return int(a)*factorial(int(a)-1)
    except ValueError:
        print("You did not enter an integer!!")


x = input("Enter an integer :   ")
print(factorial(x))
