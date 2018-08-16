#Specifying the Range for Fibonacci Sequence
num = int(input('Enter the Range you want to get Fibonacci :'))
#Defining Function Fibonacci as fibo()
def fibo():
	#Initializing the values
	a,b = 0,1
# Specifying limit for Fibonacci Sequence
	while(a<num):
	#print the values
		print(a)
	#Swapping the values
		a,b = b,a+b	
#Calling the function fibo()
fibo()
