# Mixing Positional and Arbitary Arguments

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a {0}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("\t- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')