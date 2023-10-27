# Найти в массиве не повторяющийся элемент без использования [i], set, sort, count, index.


def d(arr):
    n = None
    while (len(arr) > 0):
        n = max(arr)
        arr.remove(max(arr))
        if n in arr:
            arr.remove(n)
        else:
            break
    return n


arr = [2, 2, 1, 3, 3, 4, 4]
print(d(arr))
arr = [2, 2, 1, 1, 9, 3, 3, 4, 4]
print(d(arr))
arr = ["A", "A", "B", "B", "C", "D", "D"]
print(d(arr))
