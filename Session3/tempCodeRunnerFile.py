from ast import keyword


l=["Fsmv&u","i-zU","i!!Au","İ&!@u"]
unwanted_chars="!?-*+/@&%"
txt=" ".join(l)
print(txt)
for x in unwanted_chars:
    if x in txt:
        txt=txt.replace(x,"")
print(txt)

keywords=(txt.lower())
print(keyworda)