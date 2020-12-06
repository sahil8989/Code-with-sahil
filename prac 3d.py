def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1) 
 
def rfactor(n,i):
	if i<=n:
		if n%i==0:
			print(i)
		rfactor(n,i+1)

def itrfact(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact*i
	return fact

def i_factors(n):
    i = 1
    while(i < n+1):
        if n % i == 0:
            print(i)
        i = i + 1

print ("To find the factorial and all factors of a number")
v=input("Enter the (R) for using Recursion and (I) for Iteration:")
if v in ("i", "I", "r", "R"):
	num = int(input("Enter no. "))
	if v=="r" or v=="R":
		print("Factorial ",num," using Recursion")
		print(recur_factorial(num))
		print("factors of ",num," using Recursion")
		rfactor(num,1)
	elif v=="i" or v=="I":
		print("Factorial ",num," using Iteration")
		print(itrfact(num))
		print("factors of ",num," using Iteration")
		i_factors(num)
	else:
		print("Invalid Choice")
else:
	print("Invalid choice")
		
