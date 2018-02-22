sandwich_orders = ['Bacon Sandwich', 'Bánh mì', 'Sabich', 'Primanti', 'Polish boy']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your {0}.".format(current_sandwich))
    finished_sandwiches.append(current_sandwich)

print("\nYour sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print("\t- {0}".format(sandwich))