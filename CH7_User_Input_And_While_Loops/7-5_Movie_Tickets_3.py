prompt = "Please tell us your age for price of ticket."
prompt += "\n(Enter 'quit' to exit)\nAge: "

while True:
    ans = input(prompt)

    if ans == 'quit':
        active = False
        print('Thank you for enquiry.\n')
        break
    elif not ans.isdecimal():
        print('Please insert valid input.\n')
    else:
        age = int(ans)
        if 0 <= age < 3 :
            print('The ticket is free\n')
        elif 3 <= age <= 12 :
            print('The ticket is $10\n')
        elif age >= 12 :
            print('The ticket is $15\n')
        else:
            print('Please enter valid age\n')