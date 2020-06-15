import string
import random


def pass_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


print(pass_gen(int(input('How many characters in your password?'))))
