f=open("D:\\Documents\\Codes\\DataScienceBootcamp\\Session3\\t1.txt",'r')
#text=f.read() # read all content as a one big chunck of text
line =f.readline()  # store one line type : str
lines =f.readlines() # store all line type : list of strs
#print("#Read",text)
print("#line",line)
print("#lines",lines) 

f.close()

# file in loop
f=open("D:\\Documents\\Codes\\DataScienceBootcamp\\Session3\\t1.txt",'r')
for l in f :
    print("++",l)
    print("\n++",type(l))
f.close()

# f (file) as iterator (Occure error) // for huge data - save memory
f=open("D:\\Documents\\Codes\\DataScienceBootcamp\\Session3\\t1.txt",'r') 
print("1-",next(f))
print("2-",next(f))

f.close()
#ملاحظة : استخدم اكسبشن بدل الكاونتر في الاشياء التي تحدث خطا

