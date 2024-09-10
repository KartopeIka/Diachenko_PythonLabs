size = 7#непарне число
masiv=[[size//2+1+i for j in range(size)]for i in range(size)]
for i in range(-1, -size//2, -1):
    for j in range(size):
        masiv[i][j] = size//2-i
for row in masiv:
    print(row)