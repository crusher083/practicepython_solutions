# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random

a = [random.randint(1, 100) for x in range(10)]
b = [random.randint(1, 100) for x in range(12)]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(sorted(c))

def remove_dup(lst1, lst2):
    new_lst = [i for i in set(a) if i in b]
    return new_lst
print(remove_dup(a, b))