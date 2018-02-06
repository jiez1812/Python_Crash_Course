usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello {0}, would you like to see a status report?'.format(username))
        else:
            print('Hello {0}, thank you for logging in again.'.format(username))
else:
    print('We need to find some users!')