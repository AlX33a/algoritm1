def selection_sort(lst: list) -> list:
 
    operations_count = 0
 
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i] and i < j:
                lst[i], lst[j] = lst[j], lst[i]
            operations_count += 1
 
    print('Кол-во операций (выбором): ', operations_count)
    return lst

selection_sort(lst)
