# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def less_five(lst):
    new_lst = [n for n in lst if n < 5]
    print(new_lst)
    count = int(input('How many numbers do you want in new list?'))
    print(new_lst[:count])
