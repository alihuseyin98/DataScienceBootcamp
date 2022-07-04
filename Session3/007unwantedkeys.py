from ast import keyword


l=["Fsmv&ü","i-zÜ","i!!Aü","İ&!@ü","i"]
unwanted_chars="!?-*+/@&%"
txt=" ".join(l)
print(txt)
for x in unwanted_chars:
    if x in txt:
        txt=txt.replace(x,"")
print(txt)

keywords=(txt.lower().split())
print(keywords)
unwanted_letters=["i","ü"]
print([x for x in keywords if x not in unwanted_letters])