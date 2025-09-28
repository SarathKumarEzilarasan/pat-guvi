def print_pairs(lst):
    for i in range(len(lst)): # o(8*8) -> o(n*n) -> o(n2)
        for j in range(len(lst)):  # o(8)
            print(lst[i], lst[j])



numbers = [1, 2, 4, 10, 100, 101, 102, 103]
#             i  j


print_pairs(numbers)


# Time Complexity -> o(n2)