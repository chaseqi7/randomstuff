n=input("pls input rows and cols")
standardList=list()
for x in range(0, n):
	standardList.append("o")
first=0
last=n-1
for x in range(0, n):
	new_list = list(standardList)
	new_list[first]="i"
	new_list[last]="i"
	print new_list
	first=first+1
	last=last-1