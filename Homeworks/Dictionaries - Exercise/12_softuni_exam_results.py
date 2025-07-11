students = {}


while "exam finished" not in (line := input().split("-")):
    username = line[0]

    if "banned" in line:
        students[username]["is_banned"] = True
        continue

    language = line[1]
    points = int(line[2])

    if username in students:
        if students[username]["points"] < points:
            students[username].update({"points": points})
        students[username]["language"].append(language)
        continue
    else:
        students[username] = {"language": [language], "points": points}

print(f"Results:")
for name, info in students.items():
    if "is_banned" not in info:
        print(f"{name} | {info['points']}")

language_counter = {}

print("Submissions:")
for info in students.values():
    for lang in info["language"]:
        if lang in language_counter:
            language_counter[lang] += 1
        else:
            language_counter[lang] = 1

for lang, count in language_counter.items():
    print(f"{lang} - {count}")