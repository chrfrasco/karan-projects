"""
python implementations of the bubble sort and
merge sort algorithms.

made using psuedocode from wikipedia.

these functions only work on lists of ints.

author: christian scott
"""

def insertion_sort(l):
    for j in range(len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] > key:
            l[i + 1] = l[i]
            i = i - 1
        l[i + 1] = key
    return l

def reverse_insertion_sort(l):
    for j in range(len(l), -1, -1):
        key = l[j]
        i = j + 1
        while i <= len(l) and l[i] > key:
            l[i - 1] = l[i]
            i = i + 1
        l[i - 1] = key
    return l

def bubble_sort(l):
    n = len(l)
    while True:
        swapped = False
        for i in range(1, n):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                swapped = True
        if not swapped:
            break
    return l


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]

    while left:
        result += [left[0]]
        left = left[1:]
    while right:
        result += [right[0]]
        right = right[1:]

    return result


def merge_sort(l):
    if len(l) <= 1:
        return l
    left, right = [], []
    for i, v in enumerate(l):
        if i % 2 == 0:
            right += [v]
        else:
            left += [v]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
