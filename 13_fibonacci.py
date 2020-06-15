def fibonacci():
    while True:
        try:
            n = int(input("Enter number: "))
        except ValueError:
            print('Please enter integer')
        else:
            break
    f = [0, 1]
    if n < 0:
        print('Incorrect input!')
    elif n == 0:
        return f[0]
    elif n == 1:
        return f[1]
    else:
        for i in range(1, n + 1):
            f.append(f[i - 1] + f[i])
            print(f[i])
    return f[n]


print(f'result = {fibonacci()}')
