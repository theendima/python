def analize(numbers):
    obg = 0
    for number in numbers:
        if number % 2 == 0:
            obg += 1
    return obg

numbers = [5, 12, 8, 3, 20, 7, 12, 4]
print(analize(numbers))