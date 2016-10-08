counter=input("how many lines you want to print")
lineCounter=0
flist=list()
flist=[1]
for x in range(1,counter):
	print flist
	newList=list(flist)
	newList.append(1)
	newList[0]=1
	newList[x]=1
	for y in range(1,x):
		newList[y]=flist[y]+flist[y-1]
	flist=newList