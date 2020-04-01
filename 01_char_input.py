# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime


def hundred_years():
    name = input("Enter name: ")
    while True:
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    year = datetime.datetime.today().year
    hundred_years = year + abs(age - 100)
    print(f'{name}, in {hundred_years} you will be hundred years old!')
    while True:
        try:
            print_times = int(input("How many times you\
                                     want to reprint last sentence"))
        except ValueError:
            print('Please enter integer')
        else:
            break
    for i in range(0, print_times):
        print(f'\n{name}, in {hundred_years} you will be hundred years old!')
