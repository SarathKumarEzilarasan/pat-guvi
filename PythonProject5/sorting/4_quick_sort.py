def partition(lst, low, high): # o(n)
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def sort(lst, low, high): # o(n log n)
    if low < high:
        p = partition(lst, low, high) # o(n)
        sort(lst, low, p - 1)  # o(log n)
        sort(lst, p + 1, high)  # o(log n)


numbers = [1001, 2, 4, 10, 100, 101, 102, -103]
sort(numbers, 0, len(numbers) - 1)
print(numbers)

# Time Complexity -> o(n log n)
# Space Complexity -> o(1)
