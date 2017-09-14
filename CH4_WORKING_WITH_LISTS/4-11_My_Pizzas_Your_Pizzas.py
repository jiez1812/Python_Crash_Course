pizzas = ["neapolitan", "chicago", "new york style", "sicilian", "greek", "california", "tomato pie"]
friend_pizzas = pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("carbonara")

print("My favorite pizzas are:")
for pizza in pizzas:
    print("\t" + pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print("\t" + friend_pizza)