import re

n = int(input())
attacked = []
destroyed = []

pattern = re.compile(
    r'@(?P<planet>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<attack_type>A|D)![^@\-!:>]*->(?P<soldiers>\d+)'
)

for _ in range(n):
    message = input()

    key = sum(message.lower().count(ch) for ch in 'star')

    decrypted = ''.join(chr(ord(c) - key) for c in message)

    match = pattern.search(decrypted)
    if match:
        planet = match.group('planet')
        attack_type = match.group('attack_type')
        if attack_type == 'A':
            attacked.append(planet)
        elif attack_type == 'D':
            destroyed.append(planet)

attacked.sort()
destroyed.sort()

print(f"Attacked planets: {len(attacked)}")
for planet in attacked:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed)}")
for planet in destroyed:
    print(f"-> {planet}")
