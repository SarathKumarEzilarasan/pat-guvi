def merge(lst, low, mid, high):
    lst1 = lst[low:mid + 1]
    lst2 = lst[mid + 1: high + 1]
    n1, n2 = len(lst1), len(lst2)

    i = j = 0
    k = low

    while i < n1 and j < n2:  # o(n + n) -> o(2n) ->  o(n)
        if lst1[i] < lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1
        k += 1
    while i < n1:  # o(n)
        lst[k] = lst1[i]
        i += 1
        k += 1

    while j < n2:  # o(n)
        lst[k] = lst2[j]
        j += 1
        k += 1


def sort(lst, low, high):  # o(log n) * o(n) -> o(n log n)
    if low < high:
        mid = (low + high) // 2
        sort(lst, low, mid) # o(log n)
        sort(lst, mid + 1, high) # o(log n)
        merge(lst, low, mid, high) # o(n)


numbers = [1001, 2, 4, 10, 100, 101, 102, -103]

sort(numbers, 0, len(numbers) - 1)

print(numbers)

# Time Complexity -> o(n log n)
# Space Complexity -> o(n)
