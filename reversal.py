
# The following program accepts string input from the user and returns the string reversed.
# example : dog - god.


def reverse():
    result = ''
    word = input("Enter the data you need reversed :  ")
    for i in range(len(word)):
        ind = (len(word)-1)-i
        result += word[ind]
    print("Your reverse is :")
    print(result)


reverse()

