'''
这道题是第八章，8-15题
'''

def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with the following topping:")
    for topping in toppings:
        print(f'-{topping}')

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers')


