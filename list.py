x = [10, 20, 30, 40, 50]
print(x[0], x[2],x[-1])

numbers = [1, 2, 3]
numbers.append([4,5,6]) #прикол =)

print(numbers)

numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
numbers.append(6)
print(numbers)

numbers = [1, 2, 3]
numbers2 = [4,5,6]
print(numbers + numbers2)

numbers = [10, 5, 8, 20, 3]
maxim = 0
for i in numbers:
    if maxim < i:
        maxim = i
print(maxim)