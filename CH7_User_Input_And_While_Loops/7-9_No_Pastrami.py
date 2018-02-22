sandwich_orders = ['Bacon Sandwich', 'Pastrami', 'Bánh mì', 'Sabich', 'Pastrami', 'Primanti', 'Pastrami', 'Polish boy']
finished_sandwiches = []
run_out_sandwich = 'Pastrami'

print("The deli has run out of {0}\n".format(run_out_sandwich))
while run_out_sandwich in sandwich_orders:
    sandwich_orders.remove(run_out_sandwich)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your {0}.".format(current_sandwich))
    finished_sandwiches.append(current_sandwich)

print("\nYour sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print("\t- {0}".format(sandwich))