customers=[["hasan",[20,40,50,60]],["alma",[40,30]],["ali",[70,10,20]],["ziad",[25,60,40,50,12]]]

#name of the customer who paid more :
#1 
payments=list(map(lambda c : sum(c[1]),customers))
print("#1 customer who paid more :",customers[payments.index(max(payments))][0])

#2
print("Sorted",sorted(customers, key=lambda c:sum(c[1]))[-1][0])
l2=sorted(customers, key=lambda c:sum(c[1]))
print("#2",l2[-1][0])


#total payments made by all customers :
#summ=0
#ll=[sum(c[1]) for c in customers]
#1
print("#1 total payments :",sum([sum(c[1]) for c in customers]))
#2
print("#2 ",sum(list(map(lambda c : sum(c[1]),customers))))