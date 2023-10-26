# I need a wristband. Help me in identifying an actual wristband.
# Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.

def is_wristband(arr):
    b1 = True
    b2 = True
    b3 = True
    b4 = True
    for i in range(len(arr)):
        for j in range(len(arr[i]) - 1):
            if not (arr[i][j] == arr[i][j + 1]):
                b1 = False
                break
        for i in range(len(arr[0])):
            for j in range(len(arr) - 1):
                if not (arr[j][i] == arr[j + 1][i]):
                    b2 = False
                    break
        for i in range(len(arr) - 1):
            for j in range(len(arr[i]) - 1):
                if not (arr[i][j] == arr[i+1][j+1]):
                    b3 = False
                    break
        for i in range(len(arr) - 1):
            for j in range(1, len(arr[i])):
                if not (arr[i][-j] == arr[i + 1][-j - 1]):
                    b4 = False
                    break
    return b1 or b2 or b3 or b4


arr1 = [
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "B", "A"]
]
arr2 = [
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "B", "A"]
]
arr3 = [
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "B", "A"]
]
arr4 = [
    ["A", "B", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["A", "B", "A"]
]
print(is_wristband(arr1))
print(is_wristband(arr2))
print(is_wristband(arr3))
print(is_wristband(arr4))
