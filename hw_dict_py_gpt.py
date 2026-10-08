user = {
    "name": "Dima",
    "age": 31,
    "city": "Tiraspol",
    "experience": 5,
    "job": "engineer"
}
user["age"] += 1
user["job"] = "Python Developer"

print(user)
for key, value in user.items():
    print(f"{key}: {value}")




for key, value in user.items():
    if isinstance(value, int):
        print(f"{key}-> {value}")



users = {
    "Dima": 31,
    "Alex": 25,
    "Sergey": 42,
    "Anna": 19,
    "Max": 35
}
old = 0
for key, value, in users.items():
    if value > 30:
        old += 1
print(old)



for key, value in users.items():
    if value > 30:
        print(f"{key}-> {value}")




users = [
    {"name": "Dima", "age": 31},
    {"name": "Alex", "age": 25},
    {"name": "Sergey", "age": 42},
    {"name": "Anna", "age": 19},
    {"name": "Max", "age": 35}
]

for user in users:
    if user["age"] > 30:
        print(f"{user['name']} -> {user['age']}")


users = [
    {
        "name": "Dima",
        "age": 31,
        "skills": ["Python", "Git"]
    },
    {
        "name": "Alex",
        "age": 25,
        "skills": ["HTML", "CSS"]
    },
    {
        "name": "Sergey",
        "age": 42,
        "skills": ["Python", "Django", "SQL"]
    },
    {
        "name": "Anna",
        "age": 29,
        "skills": ["JavaScript", "React"]
    },
    {
        "name": "Max",
        "age": 35,
        "skills": ["Python", "Django"]
    }
]
pyth_true = []
for user in users:
    if user["age"] > 30 and "Python" in user["skills"]:
        pyth_true.append(user)
print(pyth_true)

users = [
    {
        "name": "Dima",
        "age": 31,
        "skills": ["Python", "Git"],
        "salary": 800
    },
    {
        "name": "Alex",
        "age": 25,
        "skills": ["HTML", "CSS"],
        "salary": 600
    },
    {
        "name": "Sergey",
        "age": 42,
        "skills": ["Python", "Django", "SQL"],
        "salary": 1500
    },
    {
        "name": "Anna",
        "age": 29,
        "skills": ["JavaScript", "React"],
        "salary": 1200
    },
    {
        "name": "Max",
        "age": 35,
        "skills": ["Python", "Django"],
        "salary": 1100
    }
]

python_up_money = []
for user in users:
    if user["salary"] > 800 and "Python" in user["skills"]:
        python_up_money.append(user)
print(python_up_money)



users = [
    {"name": "Dima", "age": 31, "skills": ["Python", "Git"], "salary": 800},
    {"name": "Alex", "age": 25, "skills": ["HTML", "CSS"], "salary": 600},
    {"name": "Sergey", "age": 42, "skills": ["Python", "Django", "SQL"], "salary": 1500},
    {"name": "Anna", "age": 29, "skills": ["JavaScript", "React"], "salary": 1200},
    {"name": "Max", "age": 35, "skills": ["Python", "Django"], "salary": 1100}
]

def average_python_salary(users):
    count = 0
    total = 0

    for user in users:
        if "Python" in user["skills"]:
            count += 1
            total += user["salary"]

    return total / count

users = [
    {"name": "Dima", "age": 31, "skills": ["Python", "Git"], "salary": 800},
    {"name": "Alex", "age": 25, "skills": ["HTML", "CSS"], "salary": 600},
    {"name": "Sergey", "age": 42, "skills": ["Python", "Django", "SQL"], "salary": 1500},
    {"name": "Anna", "age": 29, "skills": ["JavaScript", "React"], "salary": 1200},
    {"name": "Max", "age": 35, "skills": ["Python", "Django"], "salary": 1100}
]

result = average_python_salary(users)
print(result)




def get_python_high_salary_users(users):
    result = []
    for user in users:
        if "Python" in user["skills"] and user["salary"] > 1000:
            result.append(user["name"])
    return result


def adult(name):
    if name["age"] > 18:
        return f"{name['name']} Взрослый"
    else:
        return f"{name['name']}  не взрослый"

user = {
    "name": "Dima",
    "age": 31,
    "city": "Tiraspol",
    "experience": 5
}

print(adult(user))


def get_even_numbers(numbers):
    spice = []
    for number in numbers:
        if number % 2 == 0:
            spice.append(number)
    return spice

numbers = [4, 7, 2, 9, 1, 12, 5]
print(get_even_numbers(numbers))


def get_python_users_salary(users):
    users_old = []
    for user in users:
        if user["age"] > 30 and "Python" in user["skills"] and user["salary"] > 1000:
            users_old.append(user["name"])
    return users_old

