number_of_snowballs = int(input())
highest = 0
ball_weight = 0
ball_flying = 0
quality = 0


for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    flying_time_snowball = int(input())
    quality_of_snowball = int(input())

    formula = int((snowball_weight / flying_time_snowball) ** quality_of_snowball)

    if formula > highest:
        ball_weight = snowball_weight
        ball_flying = flying_time_snowball
        quality = quality_of_snowball
        highest = formula

print(f"{ball_weight} : {ball_flying} = {highest} ({quality})")

