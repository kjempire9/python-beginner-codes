
# This is a program that takes users input of an year and checks whether the entered year is a leap year or not


def leap_year():
    x = input("Enter the year in question :  ")
    try:
        if int(x) % 4 == 0:
            print("The year "+str(x)+" is a leap year!!")

        elif int(x) % 4 != 0:
            print("The year "+str(x)+" is NOT a leap year!!!")
    except ValueError:
        print("You did not enter an integer!!!")


leap_year()









