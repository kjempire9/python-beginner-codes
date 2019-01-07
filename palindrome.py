

# The following code checks whether a certain input is palindrome i.e racecar =racecar.
# Returns true if the input remain the same even when written backwards.

def palindrome(a):
    if a == a[::-1]:
        print('True')
    else:
        print("False")


x = input("Enter input :  ")
palindrome(x)
