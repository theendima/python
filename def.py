def hello():
    print("Привет, Python!")
    
hello()
hello()



def hello(name):
    print(f"Привет, {name}")
    
hello("Alex")
hello("John")


def add(a, b):
    return a+b
    
print(add(1,2))