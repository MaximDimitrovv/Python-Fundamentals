string_numbers = input().split(", ")

print(f"Positive: ", end="")
positive = list(positive for positive in string_numbers if int(positive) >= 0)
print(", ".join(positive))

print(f"Negative: ", end="")
negative = list(negative for negative in string_numbers if int(negative) < 0)
print(", ".join(negative))

print(f"Even: ", end="")
even = list(even for even in string_numbers if int(even) % 2 == 0)
print(", ". join(even))

print(f"Odd: ", end="")
odd = list(odd for odd in string_numbers if int(odd) % 2 != 0)
print(", ".join(odd))


