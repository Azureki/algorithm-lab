def bin_search(lst, tar, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if tar > lst[mid]:
        return bin_search(lst, tar, mid + 1, right)
    elif tar < lst[mid]:
        return bin_search(lst, tar, left, mid - 1)
    else:
        return mid


def binsearch2(lst, tar):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if tar > lst[mid]:
            left = mid + 1
        elif tar < lst[mid]:
            right = mid - 1
        else:
            return mid

    return -1


# ======= 测试 ========

# tar = 3
# # tar = 13
# L = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
# # 365 ns ± 7.71 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# print(bin_search(L, tar, 0, len(L) - 1))

# # 334 ns ± 11.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# # print(binsearch2(L, tar))

# # %timeit bisect.bisect_left(L,tar)
# # 227 ns ± 3.79 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# import bisect

# print(bisect.bisect_left(L, tar))


if __name__ == "__main__":
    import random
    lst = [random.randint(0, 10000) for _ in range(100000)]
    lst.sort()

    def test_recursion():
        bin_search(lst, 999, 0, len(lst) - 1)

    def test_loop():
        binsearch2(lst, 999)

    import timeit
    t1 = timeit.Timer("test_recursion()",
                      setup="from __main__ import test_recursion")
    t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")

    print("Recursion:", t1.timeit())
    print("Loop:", t2.timeit())

    # 递归3s
    # 循环2s
    # 内置 0.5s
