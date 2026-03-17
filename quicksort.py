def quicksort(arr):
    """使用快速排序算法对列表进行排序。

    参数:
        arr: 待排序的列表

    返回:
        排序后的新列表

    平均时间复杂度: O(n log n)，最坏情况: O(n^2)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    print("排序前:", data)
    print("排序后:", quicksort(data))
