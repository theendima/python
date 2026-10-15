users = [
    {"name": "Alex", "age": 25},
    {"name": "Maria"},
    {"name": "John", "age": 30}
]

for user in users:
    try:
        if user["age"] >= 18:
            print(user["name"], user["age"])
    except KeyError:
        print(f"Ошибка и так отсутствует в списке.")


'''Но есть вариант проще
Если отсутствие возраста — ожидаемая ситуация, необязательно использовать исключения:
for user in users:
    if user.get("age") is not None and user["age"] >= 18:        
        print(user["name"], user["age"])



Здесь user.get("age") вернёт None, если ключа нет. Проверка is not None не позволит сравнить None с числом.
Разница в подходах:
- try/except — когда операция может вызвать исключение, которое нужно обработать.
- get() и проверка — когда отсутствие ключа является обычной ситуацией и мы хотим её заранее проверить.'''