# List comprehesion
customers = ['Andile', 'Eric', 'Proud', 'Nandipa', 'Phumz']
ages = [22, 25, 20, 20, 21]
flavors = ['Strawberry', 'Banana', 'Raspberry', 'Chocolate', 'Cherry']

combined = zip(customers, ages, flavors)
customers_ice_cream = list(combined)

for cust in customers_ice_cream:
    print("{} is {} years old and prefers {}".format(*cust))
