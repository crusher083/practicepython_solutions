# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

a = [random.randint(1, 15) for x in range(random.randint(1, 10))]
b = [random.randint(1, 15) for x in range(random.randint(1, 12))]
c = [n for n in set(a) if n in b]
print(a, b, c, sep='\n')
