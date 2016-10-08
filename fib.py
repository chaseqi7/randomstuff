counter=input("which one you want to print")
a=0
b=1
c=0
d=1
n=0
m=0
while m<counter:
	if(m%2==0):
		if(m==counter-1):
			print c
		c=c+d
		m=m+1
	if(m%2==1):
		if(m==counter-1):
			print d
		d=c+d
		m=m+1
		
while n<counter:

	print a
	a=a+b
	n=n+1
	if(n<counter):
		print b
		b=a+b
		n=n+1



