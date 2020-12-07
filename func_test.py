#!python
# Let's see wassup
# function to print my name

def print_fav_num(name):
    data = int(input(f"What is your favorite number {name}? "))
    return data

def add_two_numbers(a, b):
    sum = a + b
    return sum

def global_func():
    name = print_fav_num('Andile')
    num  = add_two_numbers(4, 5)
    return name, num
