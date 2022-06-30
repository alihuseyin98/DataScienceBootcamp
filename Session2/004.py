v=[20,30,4,15,8]
def f(x):
    return True
print(list(filter(lambda x : x>10,v)))

e=[["ali",4400],["musa",7000],["huseyin",4000],["salah",2000]]
print(list(filter(lambda n:n[1]>3000,e)))
def lc(x):
    return x[-1]
print(sorted(e,key=lambda x:x[-1]))
e=["ali","huseyin","salah","sasa"]
e=[["hasan",[88,70,60]],["alma",[60,66,70]],["william",[80,50,78]],["ali",[100,100,100]]]
print(min(e,key=lambda x:sum(x[-1])/3))
def la(x):
    return x[-1]

