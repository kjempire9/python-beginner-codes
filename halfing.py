

# The following codes takes a input and returns half the input.
# For example :
#               karomo - kar, 87523 - 87


def half(a):
    val = ''
    val += a[0:int(len(a)/2)]
    print(val)


x = input("Enter your input:  ")
half(x)
