current_users = ['ADMIN', 'JOHN', 'CHRIS', 'MICHELLE', 'FIONA']
new_users = ['ROSE', 'FIONA', 'RAY', 'MIZUKI', 'CHRIS']

for new_user in new_users:
    if new_user.upper() in current_users:
        print('Please enter a new username')
    else:
        print('This username is available.')