'''
这道题是第八章，8-16题
'''
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers')

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushroom', 'green peppers')

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers')

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers')



