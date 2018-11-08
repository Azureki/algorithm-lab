from queue import PriorityQueue


class Node:
    def __init__(self, left, right, freq, char=None):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq


def huffman_coding(pq):
    n = pq.qsize()
    for i in range(n - 1):
        l, r = pq.get(), pq.get()
        node = Node(l, r, l[0] + r[0])

        pq.put((l[0] + r[0], node))

    return pq.get()


data = []

# read data
# 10 testcases, each case has 10k characters
with open('data.txt', 'r', encoding='utf8') as f:
    data = [f.read(10000) for _ in range(10)]

d = {}
for c in data[0]:
    if d.get(c):
        d[c] += 1
    else:
        d[c] = 1

# print(d)
pq = PriorityQueue()
for k, v in d.items():
    node = Node( None, None, v,char=k)
    pq.put((v, node))

print(pq.qsize())
print(len(d))
print(huffman_coding(pq))
