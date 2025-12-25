import calc as calc

def test_add():
    if calc.add(2, 3) == 5:
        print("Тест функции сложения пройден")
    else:
        print("Тест функции сложения НЕ пройден")
test_add()