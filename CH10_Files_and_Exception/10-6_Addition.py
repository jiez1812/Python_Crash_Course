try:
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))

    sum = num1 + num2
except ValueError:
    print("please enter number.")
else:
    print(sum)