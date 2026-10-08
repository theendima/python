def add(*args): # tuple
    sum = 0
    for i in args:
        if i % 2 == 0:
            sum += 1
    return sum

values = [1, 2, 3, 4, 5]
other_values = [6,7,8,9,10]
print(add(*values, *other_values))


def introdice(**kwargs): #  kwargs  словарь
    for key, value in kwargs.items():
        print(key, value)

guest = {
    "name": "Dima",
    "Age": 31,
    "city": "TIraspol"


}
introdice(**guest)



