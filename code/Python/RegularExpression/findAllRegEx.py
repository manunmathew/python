import re

word = "mymymym phone number is 9876543 and my pin code 689513"
#rule = r'\d+'
#rule = r'\D+'
#rule = '[+][9][1][987]{1}[0-9]{9}'
rule = 'ym'
y = re.findall(rule, word)

print(y)
