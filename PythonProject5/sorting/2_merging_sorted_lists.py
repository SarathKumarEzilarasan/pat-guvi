# o(n) + o(n) + o(n) -> o(3n) -> o(n)
def merge_lists(lst1, lst2):
    i = j = 0

    merged = []
    n1, n2 = len(lst1), len(lst2)

    while i < n1 and j < n2: # o(n + n) -> o(2n) ->  o(n)
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    while i < n1:   # o(n)
        merged.append(lst1[i])
        i += 1

    while j < n2:   # o(n)
        merged.append(lst2[j])
        j += 1

    return merged


lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8]

print(merge_lists(lst1, lst2))

# Time Complexity -> o(n)