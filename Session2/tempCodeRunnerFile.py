customers=[["hasan",[20,40,50,60]],["alma",[40,30]],["ali",[70,10,20]],["ziad",[25,60,40,50,12]]]

#name of the customer who paid more :
#1 
payments=list(map(lambda c : sum(c[1]),customers))
print("customer who paid more :",customers[payments.index(max(payments))][0])
#print(list(map(lambda c : sum(c[1]),customers)))
#2
l2=sorted(customers, key=lambda c:sum(c[1]))