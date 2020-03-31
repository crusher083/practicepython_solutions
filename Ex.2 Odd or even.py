# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
def odd_or_even():
    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    if num % 4 == 0:
        print('Number is divisible by 4')
    elif num % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')
    while True:
        try:
            check = int(input("Enter check-number: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    if num % check == 0:
        print('Divisible')
    else:
        print('Nope')
