# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import numpy
import numpy as np

def day0():
    a = np.array([1, 2, 3])
    b = np.array([3, 2, 1])
    b.reshape(3, 1)
    c = np.dot(a, b)
    d = np.array([5, 6, 4])
    d = np.split(d, 3)
    d = [int(x[0]) for x in d]
    d = np.array(d)
    print(c)
    print(b)
    print(d)

def day1():
    print("第一题")
    a = np.arange(10)
    print(a)
    print("第二题")
    b = np.ones((3,3))
    print(b)

def day2():
    arr = np.arange(20)
    print(arr)
    ones = np.ones((3,3))
    print(ones)
    rand_int = np.random.randint(0,100,5)
    print(rand_int)
    flat = np.arange(1, 13)
    mat = np.reshape(flat,(3,4))
    print(mat)
    mat_T = mat.T
    print(mat_T)
    a = np.array([10, 20, 30, 40, 50, 60])
    b = a[2:5]
    print(b)
    b1 = a[a>=30]
    b1 = b1[b1<=50]
    print(b1)
    c = a[a%20==0]
    print(c)
    data = np.array([12, 45, 67, 89, 23, 56, 78, 90, 34, 67])
    mean_val = data.mean()
    print(mean_val)
    median_val = np.median(data)
    print(median_val)
    std_val = data.std()
    print(std_val)
    max_val = data.max()
    min_idx = data.min()
    print(max_val,min_idx)
    matrix = np.arange(1,10)
    matrix = np.reshape(matrix,(3,3))
    print(matrix)
    result = np.array([matrix[0]+10,matrix[1]+20,matrix[2]+30])
    print(result)
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    V = np.array([a[0],a[1],b[0]])
    print(V)
    c = np.array([[7, 8]])
    h = np.array([np.concat([a[0],b[0]]),np.concat([a[1],c[0]])])
    print(h)
    dirty = np.array([0, -1, 5, -3, 0, 8, -2, 7, -4, 6])
    clean = dirty[dirty>0]
    print(clean)

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    day2()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
