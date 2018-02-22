prompt = "Please tell us your age for price of ticket."
prompt += "\n(Enter 'quit' to exit)\nAge: "

active = True

while active:
    ans = input(prompt)

    if ans == 'quit':
        active = False
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