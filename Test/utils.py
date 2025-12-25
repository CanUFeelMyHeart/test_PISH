def is_even(n):
    return n % 2 == 0 # True-четное 

def greet(name):
    if not isinstance(name, str):
        raise TypeError('Имя - строка!')
    if len(name) > 1000:
        return ValueError('Имя слишком длинное')

    return f"Привет, {name}"