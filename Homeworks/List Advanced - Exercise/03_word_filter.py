text_list = input().split(" ")

print(*(text for text in text_list if len(text) % 2 == 0), sep='\n')