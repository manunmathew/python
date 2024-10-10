import re

word = "my phone number is 9876543"
rule = r'\d+'
#rule = '[+][9][1][987]{1}[0-9]{9}'

y = re.search(rule, word)

print(y)
if y:
    print('search object found')
else:
    print('Not found')
