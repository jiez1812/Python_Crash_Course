# The modulo operator divides one number by another number and returns the remainder

number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number%2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")