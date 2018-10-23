
class Linear0:
    @staticmethod
    def randomized_partition(lst, left, right):
        tem = lst[left]
        while left < right:
            while left < right and lst[right] >= tem:
                right -= 1
            lst[left] = lst[right]
            while left < right and lst[left] <= tem:
                left += 1
            lst[right] = lst[left]
        lst[left] = tem
        return left

    @staticmethod
    def randomized_select(a, p, r, k):
        if p == r:
            return a[p]
        i = Linear0.randomized_partition(a, p, r)
        j = i - p + 1
        if k <= j:
            return Linear0.randomized_select(a, p, i, k)
        else:
            return Linear0.randomized_select(a, i + 1, r, k - j)


class Linear:
    @staticmethod
    def partition(lst, left, right, x):
        tem = lst[left]
        while left < right:
            while left < right and lst[right] >= x:
                right -= 1
            lst[left] = lst[right]
            while left < right and lst[left] <= x:
                left += 1
            lst[right] = lst[left]
        lst[left] = tem
        return left

    @staticmethod
    def linear_select(a, p, r, k):

        if (r - p < 75):
            return a[p + k - 1]

        for i in range((r - p - 4) // 5 + 1):
            pass

        x = Linear.linear_select(a, p, p + (r - p - 4) // 5, (r - p - 4) // 10)
        i = Linear.partition(a, p, r, x),
        j = i - p + 1
        if k <= j:
            return Linear.linear_select(a, p, i, k)
        else:
            return Linear.linear_select(a, i + 1, r, k - j)


if __name__ == "__main__":
    import random
    import timeit
    lst = [random.randint(0, 10000) for _ in range(10000)]
    def test_my():
        Linear0.randomized_select(lst, 0, len(lst) - 1, 5)
    t1 = timeit.Timer("test_my()",
                      setup="from __main__ import test_my")

    print("我的:", t1.repeat(1,1000))
