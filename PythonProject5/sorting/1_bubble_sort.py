def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]


numbers = [1001, 2, 4, 10, 100, 101, 102, -103]

bubble_sort(numbers)
print(numbers)

# Time Complexity -> o(n2)