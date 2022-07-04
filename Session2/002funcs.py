l=[1,5,4,6,5,5]
def bro(x):
    return x**x
print(list(map(bro,l))) 
l2=["ali","huseyin","salah","yousef"]
def fc(strin):
    return strin[0]
print(list(map(fc,l2)))
print(list(map(lambda n :str(n).upper(),l2)))
#LAMBDA
print(list(map(lambda n : str(n[-1]).upper(),l2)))