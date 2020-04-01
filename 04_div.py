# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
def divisors():
    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    for n in range(1, (num + 1)):
        if num % n == 0:
            print(n)
