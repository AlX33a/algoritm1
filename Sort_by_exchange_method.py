def bubble_sort(lst: list) -> list:
    n = len(lst)
    operations_count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            operations_count += 1
    print('Кол-во операций (обменом): ', operations_count)
    return lst

bubble_sort(lst)
