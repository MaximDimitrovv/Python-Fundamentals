def is_valid(segment):
    if segment[0] == segment[-1] and segment[0] in ['=', '/']:
        content = segment[1:-1]
        if content.isalpha() and content[0].isupper() and len(content) >= 3:
            return content
    return None

text = input()
valid = []
points = 0

i = 0
while i < len(text):
    if text[i] in ['=', '/']:
        start = i
        i += 1
        while i < len(text) and text[i].isalpha():
            i += 1
        if i < len(text) and text[i] == text[start]:
            end = i
            segment = text[start:end+1]
            destination = is_valid(segment)
            if destination:
                valid.append(destination)
                points += len(destination)
            i += 1
        else:
            i = start + 1
    else:
        i += 1

print(f"Destinations: {', '.join(valid)}")
print(f"Travel Points: {points}")