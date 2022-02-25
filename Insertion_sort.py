def insertion_sort(lst: list) -> list:
    n = len(lst)
    operations_count = 0
    for i in range(1,n):
        for j in range(i, 0, -1):
            operations_count += 1
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else: break
 
insertion_sort(lst)
