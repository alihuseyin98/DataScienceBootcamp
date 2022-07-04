names=['hasan', 'ziad', 'mike', 'alma', 'noor', 'sedra', 'william','jo']
values=[10, 20, 4, 30, 60, 40, 50, 100]
other =[5,4,5,5,541,4,5,6,21132]
#zip
ziped=list(zip(names,values))
print(ziped)
#-
ziped=list(zip(names,values,other)) #no matter if any list is longer then others
print(ziped)
print("+++",list(zip(*ziped))) # separating ziped list to  :)
print("---",list(list(zip(*ziped))[0])) # separating ziped list to lists  :)

# zip return value
ziped=zip(names,values) # iterable
print(ziped)
i =iter(ziped)
print(next(i))
print(next(i)) # generate error "out of band"
print(next(i))
