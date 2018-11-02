
def lcs(X, Y):
    length1, length2 = len(X), len(Y)
    c = [[0] * (length2 + 1) for _ in range(length1 + 1)]
    # array c has been initialized
    # for i in range(length1):
    #     c[i][0] = 0
    # for j in range(length2):
    #     c[0][j] = 0
    for i in range(length1):
        for j in range(length2):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    return c


X = '23235435'
Y = '23423'
c = lcs(X, Y)
print(c, '\n=======')
ma = max(x for row in c for x in row)
print(ma)
