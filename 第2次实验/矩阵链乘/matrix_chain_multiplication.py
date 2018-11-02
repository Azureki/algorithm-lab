def print_res(s, i, j):
    if i == j:
        print('A' + str(i), end='')
    else:
        print('(', end='')
        print_res(s, i, s[i][j])
        print_res(s, s[i][j] + 1, j)
        print(')', end='')


def matrix_chain_order(p):
    n = len(p) - 1

    # matrices are 0-indexed
    m = [[None] * n for _ in range(n)]
    s = [[None] * n for _ in range(n - 1)]

    # initialized
    for i in range(n):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(p)
print(m)
print('=====')
print(s)

print_res(s, 0, 5)
