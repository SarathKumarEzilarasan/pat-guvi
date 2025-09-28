def binary_search(_numbers, low, high, _target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if _numbers[mid] == _target:
        return mid
    if _numbers[mid] > _target:
        return binary_search(_numbers, low, mid - 1, _target)
    return binary_search(_numbers, mid + 1, high, _target)


numbers = [1, 2, 4, 10, 100, 101, 102, 103]
target = 1000

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print(f"No result found at index {result}")

# Time Complexity -> o(log n)