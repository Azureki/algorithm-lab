from queue import PriorityQueue
from bisect import bisect_left


def binsearch(lst, tar):
    left, right = 0, len(lst) - 1
    mid = (left + right) // 2  # 本不需要，奇怪
    while left <= right:
        mid = (left + right) // 2
        if tar < lst[mid][0]:
            left = mid + 1
        elif tar > lst[mid][0]:
            right = mid - 1
        else:
            return mid

    if mid < 0:
        return 0
    elif mid == len(lst):
        return mid
    return mid if lst[mid][0] < tar else mid + 1


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        # self.freq = freq


def huffman_coding(pq):
    pass

    # return pq.get()


data = []

# read data
# 10 testcases, each case has 10k characters
with open('data.txt', 'r', encoding='utf8') as f:
    data = [f.read(10) for _ in range(1)]

d = {}
# data[0] = 'a' * 45 + 'b' * 13 + 'c' * 12 + 'd' * 16 + 'e' * 9 + 'f' * 5
for c in data[0]:
    if d.get(c):
        d[c] += 1
    else:
        d[c] = 1

# print(d)
# pq = PriorityQueue()
pq = [(v, k) for k, v in d.items()]
pq.sort(key=lambda t: t[0], reverse=True)
# for k, v in d.items():
#     pq.put((v, k))


n = len(pq)
for i in range(n - 1):
    l, r = pq.pop(), pq.pop()
    node = Node(l, r)
    # print(l[1],r[1])

    pq.insert(binsearch(pq, l[0] + r[0]), (l[0] + r[0], node))

root = pq.pop()
# node.left

d2 = {}


def dfs(node, depth):
    if isinstance(node[1], Node):
        dfs(node[1].left, depth + 1)
        dfs(node[1].right, depth + 1)
    else:
        d2[node[1]] = depth


dfs(root, 0)

# for k, v in d2.items():
#     print(k, v)

# print('===========')

# for k, v in d.items():
#     print(k, v)

# print(len(d))
# print(len(d2))

# ==============
# for i in d:
# 	if i in d2:
# 		pass
# 	else:
# 		print(False)
# ===========
# def dfs2(node):
# 	if isinstance(node[1], Node):
# 		print(node)
# 		dfs2(node[1].left)
# 		dfs2(node[1].right)
# 	else:
# 		print(node)


# dfs2(root)
# ===========
s1 = sum(d.values())
# print(s1)
SUM = sum([d[k] * d2[k] for k in d])
print('fixed bits length', s1 * 8)
print('dynamic bits length', SUM)

# 10
# 80 32

# 100
# 800 441

# 1000
# 8000 13279
# 8000 4921

# 10000
# 80000 45574

# 100000
# 800000 450061