"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""

#a, b, c = 2, "+", 2
a, b, c = "hello world!", "*", 2
#a, b, c = 10, ")", 2

def calculate(opd1, opr, opd2):
    if opr == '+':
        return (opd1 + opd2)
    elif opr == '-':
        return (opd1 - opd2)
    elif opr == '*':
        return (opd1 * opd2)
    elif opr == '/':
        return (opd1 / opd2)
    else:
        return None

print(calculate(a, b, c))