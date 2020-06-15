a = [1, 3, 5, 3, 5, 6, 1, 8, 7]

def remove_dup(lst):
    b = [i for i in set(a)]
    return b
def remove_dup1(lst):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return  sorted(b)
print(remove_dup(a))
print(remove_dup1(a))