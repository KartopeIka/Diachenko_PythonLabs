size = 5
masiv = [[(size // 2 + 1 + i) if (size // 2 + 1 + i) <= size else (size + size // 2  - i) for j in range(size)] for i in range(size)]
for row in masiv:
    print(row)