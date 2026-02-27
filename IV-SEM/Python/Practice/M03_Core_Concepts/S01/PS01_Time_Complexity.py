def Linear_Search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i
    return -1

print(Linear_Search([1, 2, 3, 4, 5], 3))
print(Linear_Search([1, 2, 3, 4, 5], 5))
print(Linear_Search([1, 2, 3, 4, 5], 2))
