counter=input("which one you want to print")
a=0
b=1
n=0
while n<counter:

	print a
	a=a+b
	n=n+1
	if(n<counter):
		print b
		b=a+b
		n=n+1

	

