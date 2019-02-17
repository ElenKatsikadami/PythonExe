#remove comments in python program ex.3

import re


def stripComments(code):
    code = str(code)
    return re.sub(r'#[\s\S]*?.*', '', code)

with open("C:/Users/Grah/Desktop/script.py", 'r') as f:
    content = f.read()

stripComments(content)
print(stripComments(content))

