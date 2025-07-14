team_numbers = range(1, 12)
team_a = list(team_numbers)
team_b = list(team_numbers)

penalty_cards = input()

penalty_list = penalty_cards.split(" ")
past_penalties = []

for penalty in penalty_list:
    if penalty in past_penalties:
        continue
    if "B" in penalty:
        team_b.pop()
    if "A" in penalty:
        team_a.pop()
    past_penalties.append(penalty)

    if len(team_a) < 7 or len(team_b) < 7:
        break


print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if len(team_a) < 7 or len(team_b) < 7:
  print("Game was terminated")



