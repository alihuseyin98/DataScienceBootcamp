import matplotlib.pyplot as plt
im=plt.imread(r'D:\Personal\RandomFiles\aa.jpg')
im=im.astype(int)
im[30:,:,0]=0
#print(plt.imshow(im))
plt.imshow(im)
plt.show()