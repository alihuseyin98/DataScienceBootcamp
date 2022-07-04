#Exceptions

#raise Exception
for x in range(3):# range(4):
    if x==3:
        raise Exception("range To 3 YA BROO")
    
# Handle Exception
v=[22,35,45,0,8]
for x in v:
    try:
        print(2/x)
    except:
        print("cant divide with zer0")
        
for x in v:
    try:
        print(2/x)
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("ZeroDivisionError")

# errors with functions :
def sum(x,y):
    try:
        x+y
    except TypeError:
        return int(x)+int(y)
    
print(sum("1",2))
# else:(when every thing is fine) and finally (anyway)