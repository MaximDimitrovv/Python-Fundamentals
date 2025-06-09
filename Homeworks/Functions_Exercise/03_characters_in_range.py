def characters_in_range(symbol_1, symbol_2):
    symbol_1_number = ord(symbol_1)
    symbol_2_number = ord(symbol_2)

    symbol_list = []

    for number in range(symbol_1_number + 1, symbol_2_number):
        symbol_list.append(chr(number))

    return symbol_list

first_symbol = input()
second_symbol = input()

new_list = characters_in_range(first_symbol, second_symbol)
final_string = " ".join(new_list)
print(final_string)
