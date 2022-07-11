import matplotlib.pyplot as plt
im=plt.imread(r'D:\Personal\RandomFiles\aa.jpg')

im=im.astype(int)
#	rgb(50,205,50)
im[0:50,:,[0,1,2]]=[0,255,0] #36, 135, 31
im[50:100,:,[0,1,2]]=[255,255,255]
#im[50:100,65:80,[0,1,2]]=[255,0,0]
#im[50:100,117:140,[0,1,2]]=[255,0,0]
#im[50:100,:,[0,1,2]]=[255,255,255]
im[100:150,:,[0,1,2]]=[0,0,0]

im[im>=110]=255
im[im<110]=0
#print(plt.imshow(im))
plt.imshow(im)
plt.show()

im[im<150]=255
plt.imshow(im)
im[30:,:,0]=0
plt.imshow(im)
plt.imshow(im)