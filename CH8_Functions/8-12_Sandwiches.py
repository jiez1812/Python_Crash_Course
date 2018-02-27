def order_sandwiches(*names):
    print('\nSandwich order list:')
    for name in names:
        print('\t-' + name)

order_sandwiches('Andrew', 'Kate')
order_sandwiches('William')
order_sandwiches('Mia', 'Naze', 'Hadijah')