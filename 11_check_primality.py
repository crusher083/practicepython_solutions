import math


def input_number():
    while True:
        try:
            num = int(input("Enter number: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    if check_prime(num):
        print(f'{num} is prime!')
    else:
        print(f'{num} is not prime!')


def check_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    sqrt_n = math.sqrt(n)
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    input_number()
