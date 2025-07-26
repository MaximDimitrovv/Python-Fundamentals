import re

demons = input().split(',')

results = []

for demon in demons:
    demon = demon.strip()

    health_chars = re.findall(r'[^0-9+\-*/\.]', demon)
    health = sum(ord(ch) for ch in health_chars)

    numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', demon)
    damage = sum(float(num) for num in numbers)

    for symbol in demon:
        if symbol == '*':
            damage *= 2
        elif symbol == '/':
            damage /= 2

    results.append((demon, health, damage))

results.sort(key=lambda x: x[0])

for demon, health, damage in results:
    print(f"{demon} - {health} health, {damage:.2f} damage")
