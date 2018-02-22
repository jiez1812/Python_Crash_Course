prompt = "Please tell us your age for price of ticket."
prompt += "\n(Enter 'quit' to exit)\nAge: "

ans = ""
while ans != 'quit':
    ans = input(prompt)

    if ans.isdecimal() :
        age = int(ans)
        if 0 <= age < 3 :
            print('The ticket is free\n')
        elif 3 <= age <= 12 :
            print('The ticket is $10\n')
        elif age >= 12 :
            print('The ticket is $15\n')
        else:
            print('Please enter valid age\n')
    elif ans == 'quit':
        print('Thank you for enquiry.\n')
    else:
        print('Please insert valid input.\n')