user = {
    "name": "Dima",
    "age": 31,
    "city": "Tiraspol",
    "job": "engineer"
}
for key, value in user.items():
    if isinstance(value, str): # isinstance(значение, тип) используется для проверки типа значения
        print(f"{key}: {value}")

#for key, value in user.items():
#    print(f"{key} -> {value}")



