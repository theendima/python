def fet_given(numbers):
    num = []
    for i in numbers:
        if i % 2 == 0:
            num.append(i)
    return num

numbers = [5, 12, 8, 3, 20, 7, 12, 4]

print(fet_given(numbers))