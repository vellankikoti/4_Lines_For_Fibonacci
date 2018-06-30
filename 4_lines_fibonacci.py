#Fibonacci Sequence in 4 Lines

# Defining variables and assigning values to them
a,b = 0,1
# Specifying limit for Fibonacci Sequence
while(b<50):
	#Swapping the values
	a,b = b,a+b
	#print the values
	print(a)	
