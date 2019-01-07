

# This takes in two different inputs as integers and gives the factors of the first numbers upto the
# factor of the second number.
# For example : 2 4
# results to : 2,4,6,8


def factors(a, b):
    try:
        for i in range(int(b)):
            print(int(a)*i)
    except ValueError:
        print("You did not enter an integer!!")


x = input("Enter the base :  ")
y = input("Enter the last factor :")
factors(x, y)
