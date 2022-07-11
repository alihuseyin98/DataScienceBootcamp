def sum(x,y):
    try:
        x+y
    except TypeError:
        return int(x)+int(y)
    
print(sum("1",2))