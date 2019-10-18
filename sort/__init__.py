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
    排序算法

"""

_DEBUG = True

class _BaseSort(object):
    """
    排序算法的基类
    """
    def __init__(self, *args, **kwargs):
        """
        初始化
        :param args:
        :param kwargs:
        """
        pass

    def _iterable_swap(self, iterable, i, j):
        """
        列表元素交换
        :param iterable:
        :param i:
        :param j:
        :return:
        """
        tmp = iterable[i]
        iterable[i] = iterable[j]
        iterable[j] = tmp

    def Sort(self, iterable, *args, **kwargs):
        """
        排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        return NotImplemented


class BubbleSort(_BaseSort):
    """
    冒泡排序算法
    """
    def Sort(self, iterable, *args, **kwargs):
        """
        冒泡排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        _reversed = kwargs.get("reversed", False)
        size = len(iterable)

        if _DEBUG:
            _loop_times = 0

        # 开始冒泡排序
        for i in range(size):
            _sorted = False
            for j in range(i+1, size):
                if iterable[i] < iterable[j]:
                    if _reversed:
                        self._iterable_swap(iterable, i, j)
                        _sorted = True
                else:
                    if not _reversed:
                        self._iterable_swap(iterable, i, j)
                        _sorted = True
                if _DEBUG:
                    _loop_times += 1
            # 如果后面的已经排序好了，就直接返回
            if not _sorted:
                break

        if _DEBUG:
            print("[BubbleSort] sort count:{0}".format(_loop_times))


class InsertionSort(_BaseSort):
    """
    插入排序
        1、从第一个元素开始，该元素可以认为已经被排序；
        2、取出下一个元素，在已经排序的元素序列中从后向前扫描；
        3、如果该元素（已排序）大于新元素，将该元素移到下一位置；
        4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
        5、将新元素插入到该位置后；
        6、重复步骤2~5。
    """
    def Sort(self, iterable, *args, **kwargs):
        """
        插入排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        _reversed = kwargs.get("reversed", False)
        size = len(iterable)

        if _DEBUG:
            _loop_times = 0

        for i in range(1, size):
            min_index = i
            for j in range(i-1, -1, -1):
                if iterable[j] > iterable[min_index] and not _reversed:
                    self._iterable_swap(iterable, j, min_index)
                    min_index = j
                elif iterable[j] < iterable[min_index] and _reversed:
                    self._iterable_swap(iterable, j, min_index)
                    min_index = j
                else:
                    break

                if _DEBUG:
                    _loop_times += 1

        if _DEBUG:
            print("[InsertionSort] sort count:{0}".format(_loop_times))


class ShellSort(_BaseSort):
    """
    希尔排序
     1、选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
     2、按增量序列个数k，对序列进行k 趟排序；
     3、每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。
     4、仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    """
    def Sort(self, iterable, *args, **kwargs):
        """
        希尔排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        _reversed = kwargs.get("reversed", False)
        size = len(iterable)

        k = int(size / 2)

        if _DEBUG:
            _loop_times = 0

        for step in range(k, 0, -1):
            for i in range(1, size, step):
                min_index = i
                for j in range(i-1, -1, -step):
                    if iterable[j] > iterable[min_index] and not _reversed:
                        self._iterable_swap(iterable, j, min_index)
                        min_index = j
                    elif iterable[j] < iterable[min_index] and _reversed:
                        self._iterable_swap(iterable, j, min_index)
                        min_index = j
                    else:
                        break

                    if _DEBUG:
                        _loop_times += 1

        if _DEBUG:
            print("[ShellSort] sort count:{0}".format(_loop_times))


class SelectionSort(_BaseSort):
    """
    选择排序
        初始状态：无序区为R[1..n]，有序区为空；
        第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
        该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
        使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
        n-1趟结束，数组有序化了。
    """
    def Sort(self, iterable, *args, **kwargs):
        """
        选择排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        _reversed = kwargs.get("reversed", False)
        size = len(iterable)

        if _DEBUG:
            _loop_times = 0

        for i in range(0, size):
            min_value = i
            for k in range(i+1,size):
                if iterable[min_value] > iterable[k] and not _reversed:
                    min_value = k
                elif iterable[min_value] < iterable[k] and _reversed:
                    min_value = k

                if _DEBUG:
                    _loop_times += 1

            self._iterable_swap(iterable, min_value, i)

        if _DEBUG:
            print("[SelectionSort] sort count:{0}".format(_loop_times))


class QuickSort(_BaseSort):
    """
    快速排序
        从数列中挑出一个元素，称为 “基准”（pivot）；
        重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
        在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
        递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    """
    def Sort(self, iterable, *args, **kwargs):
        """
        快速排序
        :param iterable:
        :param args:
        :param kwargs:
        :return:
        """
        _reversed = kwargs.get("reversed", False)
        size = len(iterable)

        self._partition_sort(iterable,0, size , _reversed)

    def _partition_sort(self, iterable, begin, end, reversed=False):
        """
        分区排序
        :param iterable:
        :param reversed:
        :return:
        """
        size = len(iterable)
        if end - begin <= 1 :
            return

        pivot_index = begin
        pivot_i = begin
        pivot_value = iterable[begin]
        for i in range(begin+1, end):
            print(iterable, pivot_index)
            if iterable[i] < pivot_value:
                self._iterable_swap(iterable, i, pivot_index)
                pivot_index += 1
                pivot_i = i
        self._iterable_swap(iterable,pivot_index,pivot_i)

        self._partition_sort(iterable,begin,pivot_i,reversed)
        self._partition_sort(iterable,pivot_i,end,reversed)
        #
        #print(iterable, pivot_index)
        # for i in range(pivot_index):
        #     if iterable[i] > iterable[pivot_index]:
        #         self._iterable_swap(iterable, i, pivot_index)
        #         pivot_index = i

        #print(iterable,pivot_index)

        #self._partition_sort(iterable[:pivot_index], reversed)
        #self._partition_sort(iterable[pivot_index:], reversed)

