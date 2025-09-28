def search_in_list(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


numbers = [2, 1, 9, 10, -1, 100]
target = 100

result = search_in_list(numbers, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print(f"No result found at index {result}")

# Best Case Time Complexity -> o(1)

# Worst Case Time Complexity -> o(n)
