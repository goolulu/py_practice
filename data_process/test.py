import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" numpy 生成数组 """


def test1():
    array1 = np.array([1, 23, 4, 5, 6])
    array2 = np.arange(0, 20, 2)
    array3 = np.linspace(-5, 5, 5)
    array4 = np.random.randint(10)
    array5 = np.random.randint(0, 100, 10)
    array6 = np.random.normal(50, 10, 20)
    array7 = np.array([[1], [2], [3]])
    array8 = np.zeros((3, 4))
    array9 = np.ones((3, 4))
    array10 = np.full((3, 4), 22)
    print(array1.dtype)
    # print(array2)
    # print(array3)
    # print(array4)
    # print(array5)
    # print(array6)
    # print(array7)
    # print(array8)
    # print(array9)
    # print(array10)

    print(array1 * array1)
    print(array1 - array1)


""" 切片索引 """


def test2():
    array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
    print(array1, end="\n\n")

    print(array1[:2, 1:], end="\n\n")
    print(array1[2:, :], end="\n\n")
    print(array1[:, 0:2], end="\n\n")
    print(array1[1, :2])
    pass


""" 布尔索引 """


def test3():
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    data = np.arange(0, 28).reshape(7, 4)
    print(data, end='\n\n')

    print(names == 'Bob')
    print(data[names == 'Bob'])
    print(data[names == 'Bob', 2:])
    print(data[names == 'Bob', 3])


""" Fancy indexing """


def test4():
    arr = np.arange(32).reshape(8, 4)
    print(arr, end='\n\n')
    print(arr[[0, 1, 2, 3]])
    print(arr[[0, 1], [1, 3]])
    print(arr[[1, 5, 7, 2]], end='\n\n')
    print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
    pass


""" 数组转置和轴对换 """


def test5():
    arr = np.arange(16).reshape((2, 2, 4))
    print(arr, end='\n----\n')
    print('默认')
    print(arr.transpose((0, 1, 2)), end='\n----\n')
    print('第3d不动，2d转4组，1d转2组')
    print(arr.transpose((0, 2, 1)), end='\n----\n')
    # print('第三d不懂，2d不动，1d不动')
    # print(arr.transpose((1, 0, 2)), end='\n----\n')
    print('3d不动，2d转4组，1d转2组')
    print(arr.transpose((1, 2, 0)), end='\n----\n')


""" 函数 """


def test6():

    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    z = np.sqrt(xs ** 2 + ys**2)
    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])

    result = np.where(cond, xarr, yarr)
    print(result)


def func(n):
    while n > 5:
        n -= 1
        yield n


def main():
    test6()


if __name__ == '__main__':
    for i in func(10):
        print(i)
