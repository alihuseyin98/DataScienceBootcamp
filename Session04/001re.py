# \t tab   \s space

print(r'c:\program files\new folder')
print('c:\program files\\new folder')

s="is hello world my name is ali and she is ..."
print(s.find("is"))
print(s.find("o")) # fint the first element's index
import re
print(re.findall("is",s))
print(re.search("is",s).span()) # for first element

txt='today is a nice day and the time now is 9:00am in NYC and the time is 4:00pm in Istanbul'
print(re.findall('...t.....',txt)) # every t and all next .numbers letters after/befor it
print(re.findall('t',txt))
# identifers
# . = any character, except a new line
# ? = match 0 or 1 repetition
# * = match 0 or more repretition
# + = match 1 or more repetition
# {} = match a range of number of times
# ^ = match start of a string
# $ = match at the end of the string
# Barckets [] used to specify a set of characters to match -one of it
# Parentheses () used to create a group of characters -as is it
# backslash \ to match special characters
# Vertical Bar | logical or
print(re.search('a.','aa')!=None)
print(re.search('a.','ab')!=None)
print(re.search('a.','a1')!=None)
print(re.search('a.','a#')!=None)
print(re.search('a.','a')!=None)
print(re.search('a.','a\n')!=None)
print(re.findall('is?.',"this is isss"))
print(re.search('is?s','this is isss')!=None)

# {} = match a range of number of times
print(re.search('ba{1,3}b','bb')!=None)
print(re.search('ba{1,3}b','bab')!=None)
print(re.search('ba{1,3}b','baab')!=None)
print(re.search('ba{1,3}b','baaab')!=None)
print(re.search('ba{1,3}b','baaaab')!=None)

# backslash \ to match special characters
print(re.search('a\?','abc')!=None)
print(re.search('a\.','abc')!=None)
print(re.search('a\*','abc')!=None)
print(re.search('a\+','abc')!=None)
# Special characters
# \d = match any decimal digit [0-9]
# \D = any non-digit character
# \w = any alphanumeric character
# \W = any non-alphanumeric character
# \s = any whitedpace character
# \S = any non-whitedpace character
# \t = tab
# \n = new line
txt='today is a nice day and the time now is 9:00am in NYC and the time is 4:00pm in Istanbul an I love the nice weather tiiime tiime tiiiiime'
print(re.findall("\d+",txt))
print(":".join(re.findall("\d+",txt)))

# some functions
# re.search
# re.findall
# re.split('[\s\n,\.-]+',txt)
re.findall('[a-z]+',txt)