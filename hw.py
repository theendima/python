'''Задание 2 из 5 — фильтрация словарей
Теперь проверим, как ты работаешь со списком словарей. Эта задача немного сложнее.
Есть данные сотрудников:
employees = [    {"name": "Alex", "age": 25, "salary": 1200},    {"name": "Maria", "age": 17, "salary": 1500},    {"name": "John", "age": 30, "salary": 900},    {"name": "Kate", "age": 22, "salary": 1800},    {"name": "Mike", "age": 19, "salary": 1100}]



Твоя задача: создать новый список, в который попадут только сотрудники, которые одновременно:
1. Старше или равны 18 годам.
2. Получают зарплату не меньше 1000.'''

employees = [
    {"name": "Alex", "age": 25, "salary": 1200},
    {"name": "Maria", "age": 17, "salary": 1500},
    {"name": "John", "age": 30, "salary": 900},
    {"name": "Kate", "age": 22, "salary": 1800},
    {"name": "Mike", "age": 19, "salary": 1100}
]

def find_adults(employees):
    dict_old = []

    for num in employees:
        if  num["age"] >= 18:
            dict_old.append(num)
    return dict_old

adults = find_adults(employees)
print(adults)


