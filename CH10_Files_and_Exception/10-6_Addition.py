print("Please enter two numbers to add")
print("enter 'q' to quit")

while True:
    num1 = input("Number 1 : ")
    if num1 == 'q':
        break
    num2 = input("Number 2 : ")
    if num2 == 'q':
        break

    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("please enter number.")
    else:
        print(sum)