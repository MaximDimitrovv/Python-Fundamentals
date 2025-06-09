def calculations(operator_symbol, number_1, number_2):
    if operator_symbol == "multiply":
        return number_1 * number_2
    elif operator_symbol == "divide":
        return number_1 / number_2
    elif operator_symbol == "add":
        return number_1 + number_2
    elif operator_symbol == "subtract":
        return number_1 - number_2

operator = input()
num_1 = float(input())
num_2 = float(input())

answer = calculations(operator, num_1, num_2)

print(f"{answer:.0f}")
