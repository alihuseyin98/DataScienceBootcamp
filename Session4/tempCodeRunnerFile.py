import re
txt='today is a nice day and the time now is 9:00am in NYC and the time is 4:00pm in Istanbul'
#print(re.findall('...t...',txt)) # every t and all next .numbers letters after/befor it
print(re.findall('t.*',txt))