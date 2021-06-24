"""
Calculadora Básica
"""


def calculadora(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '/':
        return num1 / num2
    if op == '*':
        return num1 * num2

print(calculadora(742, 90, '+'))