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


def linear_search(lst, tar):
    for i in range(len(lst)):
        if lst[i] == tar:
            return i
    else:
        return -1


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


if __name__ == "__main__":
    import random
    import re
    import timeit
    # import bisect

    # test case 0
    with open('bs-1.txt', mode='r') as f:
        s = f.read()

    lst = sorted([int(x) for x in re.split(r'\D+', s)])

    def test_loop():
        # binsearch2(lst, 116)
        linear_search(lst, 116)

    t0 = timeit.Timer(
        "test_loop()", setup="from __main__ import test_loop")
    print("bs-1.txt: ", t0.repeat(5))
    # [1.4320081346916078, 1.3002651325901213, 1.307026691773559,
    # 1.3088811170098706, 1.2997152931249172]

    # test case 1

    def test_case():
        # binsearch2(lst, (len(lst) - 1) // 2) # amazing, O(1) is slower than O(logn)
        binsearch2(lst, 1)
        # bisect.bisect(lst,1) # 内置的优化太强了。

    # lst = [random.randrange(100) for _ in range(100)]
    # lst = [random.randrange(10000) for _ in range(1000)]
    # lst = [random.randrange(1000000) for _ in range(100000)]

    # 100
    # [1.3053071604860433, 1.1562966332596425, 1.1440846987374584,
    #     1.1374587666221054, 1.1618917996575604]
    # # 10000
    # [2.1072359240180507, 1.9869812677025394, 1.970295106172168,
    #     2.1169288606703125, 2.1569164856167493]
    # # 1000000
    # [3.7125032394708493, 3.8461072648822294, 3.7301860766718145,
    #     3.9171311282815804, 3.631787905657813]

    # lst.sort()

    # t1 = timeit.Timer("test_case()", setup="from __main__ import test_case")
    # print("二分查找： ", t1.repeat(5))


# ======= 命令行测试 ========

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
