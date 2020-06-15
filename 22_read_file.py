from collections import Counter
with open('names.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]
    count = dict(Counter(lines))
    for k, v in count.items():
        print(str(k) + ': ' + str(v))
