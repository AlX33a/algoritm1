def shell_sort(lst: list) -> list:
    step = len(lst) // 2
    operations_count = 0
 
    while step > 0:
        for i in range(step, len(lst)):
            current_value = lst[i]
 
            if lst[i - step] > current_value:
                lst[i - step], lst[i] = lst[i], lst[i - step]
            operations_count += 1
        step //= 2
 
    print('Кол-во операций (Шелл): ', operations_count)
    return lst
