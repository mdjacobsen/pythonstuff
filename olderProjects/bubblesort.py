def bubblesort():
	y = [6,5,4,3,2,1]
	x = 1
	while x < len(y):
		for i in range(len(y)-1):
			if y[i]>y[i+1]:
				temp = y[i]
				y[i]=y[i+1]
				y[i+1]=temp
		x += 1
	print(y)
bubblesort()