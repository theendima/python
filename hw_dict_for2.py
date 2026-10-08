'''Задание:

Выведи только те элементы, где значение является числом.
Для каждого такого элемента выведи примерно так:
age: 31
salary: 12000'''


user = {
    "name": "Dima",
    "age": 31,
    "city": "Tiraspol",
    "job": "engineer",
    "salary": 12000
}


for key, value in user.items():
