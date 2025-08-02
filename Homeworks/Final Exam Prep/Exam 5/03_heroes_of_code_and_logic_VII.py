
heroes = {}
n = int(input())

for _ in range(n):
    hero = input().split()

    hero_name = hero[0]
    hero_hp = int(hero[1])
    hero_mp = int(hero[2])

    heroes[hero_name] = {"HP":hero_hp, "MP":hero_mp}

while (command := input()) != "End":
    split_command = command.split(" - ")
    action = split_command[0]
    hero_name = split_command[1]

    match action:
        case "CastSpell":
            mp_needed = int(split_command[2])
            spell_name = split_command[3]

            if mp_needed <= heroes[hero_name]["MP"]:
                heroes[hero_name]["MP"] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        case "TakeDamage":
            damage = int(split_command[2])
            attacker = split_command[3]

            heroes[hero_name]["HP"] -= damage

            if heroes[hero_name]["HP"] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                heroes.pop(hero_name)
        case "Recharge":
            amount_mp = int(split_command[2])

            heroes[hero_name]["MP"] += amount_mp

            if heroes[hero_name]["MP"] > 200:
                amount_needed = amount_mp - (heroes[hero_name]["MP"] - 200)
                heroes[hero_name]["MP"] = 200
                print(f"{hero_name} recharged for {amount_needed} MP!")
            else:
                print(f"{hero_name} recharged for {amount_mp} MP!")
        case "Heal":
            amount_hp = int(split_command[2])

            heroes[hero_name]["HP"] += amount_hp
            if heroes[hero_name]["HP"] > 100:
                amount_needed = amount_hp - (heroes[hero_name]["HP"] - 100)
                heroes[hero_name]["HP"] = 100
                print(f"{hero_name} healed for {amount_needed} HP!")
            else:
                print(f"{hero_name} healed for {amount_hp} HP!")

for hero, info in heroes.items():
    print(hero)
    hp = info['HP']
    mp = info['MP']
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")