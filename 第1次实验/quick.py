import random


class Quick():
    @staticmethod
    def __sort__(lst, left, right):

        if left > right:
            return
        j = Quick.partition(lst, left, right)
        Quick.__sort__(lst, left, j - 1)
        Quick.__sort__(lst, j + 1, right)

    @staticmethod
    def sort(lst):
        random.shuffle(lst)
        Quick.__sort__(lst, 0, len(lst) - 1)

    @staticmethod
    def partition(lst, left, right):
        tem = lst[left]
        while left < right:
            # due to lack of `--`, it seems can only use >=.
            # `>` is not ok
            # add right-=1 at end can not solve the problem
            while left < right and lst[right] >= tem:
                right -= 1
            lst[left] = lst[right]
            while left < right and lst[left] <= tem:
                left += 1
            lst[right] = lst[left]
        lst[left] = tem
        return left


# if __name__ == '__main__':
#     lst = [random.randint(0, 20000) for _ in range(2000)]
#     # print(lst)
#     Quick.sort(lst)
#     # lst.sort()
#     # print(lst)
#     l = lst
#     print(all(l[i] <= l[i + 1] for i in range(len(l) - 1)))

if __name__ == "__main__":
    lst = [random.randint(0, 100) for _ in range(10)]

    def test_my():
        Quick.sort(lst)

    def test_in():
        lst.sort()

    import timeit
    t1 = timeit.Timer("test_my()",
                      setup="from __main__ import test_my")
    t2 = timeit.Timer("test_in()", setup="from __main__ import test_in")

    print("我的:", t1.timeit())
    print("内置:", t2.timeit())
    # 我的: 16.32613764534548
    # 内置: 0.36055063123403386


# In [9]: def test():
#    ...:     lst = [random.randint(0, 100) for _ in range(10)]
#    ...:     Quick.sort(lst)
#    ...:

# In [11]: %timeit test()
# 21.7 µs ± 412 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# In [12]: def test2():
#     ...:     lst = [random.randint(0, 100) for _ in range(10)]
#     ...:     lst.sort()
#     ...:
#     ...:

# In [13]: %timeit test2()
# 12.6 µs ± 85.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# ==========

# In [14]: def test2():
#     ...:     lst = [random.randint(0, 10000) for _ in range(1000)]
#     ...:     lst.sort()
#     ...:
#     ...:

# In [15]: def test():
#     ...:     lst = [random.randint(0, 10000) for _ in range(1000)]
#     ...:     Quick.sort(lst)
#     ...:

# In [16]: %timeit test()
# 3.46 ms ± 73 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

# In [17]: %timeit test2()
# 1.45 ms ± 9.02 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
