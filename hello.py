marks = [23 ,45 ,56 ,78 ,90]

max = min = marks[0]

for i in marks:
	if i > max :
		max = i
	elif i < min :
		min = i
	else :
		pass

print ("**HELLO !!! Lets filter out highest and lowest marks from marks list ")

print ("\n* marks list = "+ str(marks))

print ("* MAX MARK: "+ str(max))
print ("* MIN MARK: "+ str(min))
