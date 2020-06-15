import pprint

with open ('primes.txt', 'r') as f:
    primes = [line.strip() for line in f.readlines()]
with open ('happy.txt', 'r') as f:
    happy = [line.strip() for line in f.readlines()]

overlap = [n for n in primes if n in happy]
for n in overlap:
    print(n, end=' ')