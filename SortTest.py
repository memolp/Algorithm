# -*- coding:utf-8 -*-

"""
MIT License

Copyright (c) 2019 JeffXun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author:
    JeffXun

Date:
    2019/10/18

Content:
    排序算法测试

"""


import random
from sort import *

# test_arr = []
# for i in range(100):
#     test_arr.append(random.randint(1, 100))

test_arr = [15, 3, 50, 42, 55, 42, 29, 80, 10, 500, 27]
#test_arr = [3, 10, 15, 27, 29, 42, 50, 55, 80, 500]
# test_arr = [21, 70, 62, 41, 69, 89, 43, 66, 68, 13, 46, 5, 30, 54, 16, 4, 69, 74, 20, 36, 48, 12, 3, 91, 14, 9, 35, 25, 78, 24, 80, 85, 37, 57, 25, 93, 7, 52, 44, 86, 6, 16, 82, 17, 68, 78, 5, 49, 38, 72, 89, 94, 62, 1, 60, 21, 23, 66, 9, 52, 62, 18, 92, 6, 90, 56, 10, 19, 76, 100, 92, 15, 21, 24, 34, 90, 65, 31, 1, 40, 70, 11, 99, 72, 88, 47, 20, 38, 30, 93, 2, 100, 100, 58, 54, 64, 20, 50, 69, 72]

# b = ShellSort()
# b = InsertionSort()
# b = SelectionSort()
b = QuickSort()
print(test_arr)
b.Sort(test_arr, reversed=True)
# b.Sort(test_arr, reversed=False)
print(test_arr)
