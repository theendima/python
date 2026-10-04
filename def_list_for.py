def sum_list(numbers):
    summa = 0
    
    for i in numbers:
        summa += i
    
    return summa

print(sum_list(numbers=[1, 2, 3, 4, 5]))



def find_max(numbers):
    maxim = 0
    for i in numbers:
        if maxim < i:
            maxim = i
    return maxim
print(find_max([10, 5, 8, 20, 3]))


def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count
print(count_even([1, 2, 4, 7, 8, 10]))