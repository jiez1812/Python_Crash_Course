while True:
    try:
        num1 = int(input("Number 1 : "))
        num2 = int(input("Number 2 : "))
    except ValueError:
        print("please enter number.")
        continue
    else:
        sum = num1 + num2
        print("Total : " + str(sum))
        break