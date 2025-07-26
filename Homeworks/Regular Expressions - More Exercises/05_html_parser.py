import re

content = input()

pattern_title = r'<title>(.*?)</title>'
pattern_body = r'<body>(.*?)</body>'
pattern_tags = r'\\n|<[^>]+>'
clean_body = ''

match_title = re.findall(pattern_title, content)

if match_title:
    print(f'Title: {match_title[0]}')
    match_body = re.findall(pattern_body, content)
    if match_body:

        match_tags = re.sub(pattern_tags,"", match_body[0])
        if match_tags:
            clean_body = match_tags
            print(f'Content: {clean_body}')