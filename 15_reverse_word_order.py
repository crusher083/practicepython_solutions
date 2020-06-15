s = 'My name is Michele'

def reverse(st):
    words = [w for w in st.split()]
    new_st = ' '.join(words[::-1])
    return new_st

print(reverse(s))