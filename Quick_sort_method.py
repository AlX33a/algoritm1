def quick_sort(lst: list, count = 0) -> list:
    if len(lst) <= 1:
        return lst
 
    elem = lst[0]
    left = list(filter(lambda x: x<elem, lst))
    center = [i for i in lst if i == elem]
    right = list(filter(lambda x: x>elem, lst))
 
    print('Кол-во операций (быстрая сортировка): ', count)
    return quick_sort(left, count + 1) + center + quick_sort(right, count + 1)
 
lst = [int(i) for i in range(100, 0, -1)]

quick_sort(lst)
