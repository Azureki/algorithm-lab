class Merge:
    @staticmethod
    def __sort__(lst, left, right):
        if right <= left:
            return
        mid = (left + right) // 2
        Merge.__sort__(lst, left, mid)
        Merge.__sort__(lst, mid + 1, right)
        Merge.merge(lst, left, mid, right)

    @staticmethod
    def sort(lst):
        Merge.aux = [None] * len(lst)
        Merge.__sort__(lst, 0, len(lst) - 1)

    @staticmethod
    # why use mid? store need less time than calculate?
    def merge(lst, left, mid, right):
        le, r = left, mid + 1
        for i in range(left, right + 1):
            Merge.aux[i] = lst[i]
        for i in range(left, right + 1):
            if le > mid:
                lst[i] = Merge.aux[r]
                r += 1
            elif r > right:
                lst[i] = Merge.aux[le]
                le += 1
            elif Merge.aux[r] < Merge.aux[le]:
                lst[i] = Merge.aux[r]
                r += 1
            else:
                lst[i] = Merge.aux[le]
                le += 1


if __name__ == "__main__":
    lst = [45, 34, 23, 86, 78, 98, 234, 12, 345, 78, 45, 123, 567]
    Merge.sort(lst)
    print(lst)
