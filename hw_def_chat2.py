def get_obw(numbers):
    summa = 0
    for i in numbers:
        if i % 2 == 0:
            summa += i
    return summa

numbers = [5, 12, 8, 3, 20, 7, 12, 4]
print(get_obw(numbers))




