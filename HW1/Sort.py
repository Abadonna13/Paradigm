def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if numbers[j] > numbers[m]:
                m = j
        numbers[i], numbers[m] = numbers[m], numbers[i]
    return numbers




def sort_list_declarative(numbers):
    return (numbers.sort(reverse=True))


numb_list = [5, 3, 7, 4, 3, 9, 1]
res = sort_list_imperative(numb_list)
print(res)
numb_list = [5, 3, 7, 4, 3, 9, 1]
res = sort_list_declarative(numb_list)
print(numb_list)