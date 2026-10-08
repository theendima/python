def func_wit_all_arg(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)


person = {
    "name":  "Dima",
    "age": 31,
    "city": "Tiraspol"


}

func_wit_all_arg(1, 2, 3, 4, 5, **person)
