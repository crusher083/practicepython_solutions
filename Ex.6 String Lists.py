# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
def pal_check():
    pal = input('Please add sentence: ')
    new_pal = [n.lower() for n in pal if n.isalpha()]
    rev_pal = ''.join(new_pal[::-1])
    new_pal = ''.join(new_pal)
    if new_pal == rev_pal:
        print("It's palindrome!")
    else:
        print('No, it is not a palindrome')
