x = [1,7,5,3,6]
y=max(x)

data = []
data.append(y)
newpoint = 0
a=1
while a < len(x):
	print("loop #%d" %a)
	nearestdistance = max(x)-min(x)
	for i in x:
		if i != y and i not in data:
			print("i=%d" %i)
			print("y=%d" %y)
			print("start nearest=%d" %nearestdistance)
			distance = abs(i-y)
			print("distance=%d" %distance)
			if distance < nearestdistance:
				nearestdistance = distance
				newpoint = i
			print("end nearest =%d" %nearestdistance)
			print("newpoint=%d" %newpoint)
	data.append(newpoint)
	y = newpoint
	a += 1
print(data)
