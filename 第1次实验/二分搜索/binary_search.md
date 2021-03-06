# <center>二分搜索实验报告</center>

<center>2016201218 孙浩</center>  
我保证没有抄袭。

## 实验目的

验证二分搜索算法的时间复杂度。

## 问题

编程实现算法：在有序序列中找出一个特定元素`target`。
输入：一个有序序列，一个要查找的元素。
输出：要查找元素`target`的位置`index`，如果没有找到，返回`-1.`

## 算法设计与分析

运用递归与分治的思想。
将序列分为两部分，如果`target`小于序列中间的元素，那么应该在左边查找，否则应该在右边。（如果刚好相等，就说明找到元素，返回即可。）
这样就把问题规模缩小了一半。重复上述步骤，问题规模缩减为`1`时，必然可以找到元素或发现元素不存在。

算法实现如下：

``` py
def bin_search(list, tar, left, right):
    if left > right:
        # 失败
        return -1
    mid = (left + right) // 2
    if tar > list[mid]:
        # 递归调用
        return bin_search(list, tar, mid + 1, right)
    elif tar < lst[mid]:
        # 递归调用
        return bin_search(list, tar, left, mid - 1)
    else:
        # 找到目标
        return mid
```

### 算法分析

#### 时间复杂度

假设输入序列的长度为 *N* ，那么最好情况时一次命中，也就是需要查找的元素刚好在中间。复杂度是*O(1)*。
最坏情况是 *O(log(N))* 。因为每次问题规模变为原来的一半，最坏情况下在问题规模为`1`时，算法结束，所以需要 *log(N)*  次。

#### 空间复杂度

需要三个额外变量，空间复杂度是*O(1)*。

## 实验设计

1. 使用给定的数据`bs-1.txt`，查找`target=116`。
2. 自己设计实验数据，测试二分搜索算法的时间，并分析结果。

## 实验结果以及分析

### bs-1.txt 数据

#### 二分查找

    [1.4320081346916078, 1.3002651325901213, 1.307026691773559,1.3088811170098706, 1.2997152931249172]

1.33 us。

#### 线性查找

    [5.922411419945757, 5.684383716101022, 6.174947921038653, 6.0503704268477065, 6.030542116053514]

5.97 us。

实验结果表明，二分查找确实比线性查找更快。

### 随机生成

采用python built-in module `random`, 生成一组随机数然后排序，作为输入。

`lst = [random.randrange(100) for _ in range(100)]`

输入序列的长度分别为$10^{2}$,$10^{4}$,$10^{6}$。

    100
    [1.3053071604860433, 1.1562966332596425, 1.1440846987374584,1.1374587666221054, 1.1618917996575604]
    10000
    [2.1072359240180507, 1.9869812677025394, 1.970295106172168, 2.1169288606703125, 2.1569164856167493]
    1000000
    [3.7125032394708493, 3.8461072648822294, 3.7301860766718145, 3.9171311282815804, 3.631787905657813]

求平均值，绘图。

![时间](bs1.png)

横坐标为`log(N)`，纵坐标为时间，可见时间正比于`log(N)`。  
实现结果表明，该二分搜素的时间复杂度为确实为`O(logN)`。

### 与内置函数的比较

*python* 有内置的二分插入模块，因为编写它的是行业大牛，做了很多优化，比如按照数据的分布采用3分、4分查找。  
因此，在数据量小（100，1000）时，与其差距不明显，但是到达$10^{4}$级别时，内置函数只需要`0.7-0.8us`，而我因为没有优化，却需要`3.7us`。

## 结论

在上面的结果分析中，我们可以发现二分搜索确实是`O(logN)`，并且比线性搜索要快；但是在和内置方法的比较中，我们也可以发现，虽然`O(logN)`是复杂度很低的算法，但仍然有优化的空间。

本次实验，手写实现了二分搜索算法，加深了对递归和循环的理解。学会了调用`python`的`random`库和`timeit`库，用来生成随机数和测试运行时间。并以此来验证了二分搜索算法的时间复杂度。