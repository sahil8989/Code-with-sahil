list1 = [45,9,6,1,74,53,56,78,89,76,23]
print("List = ",list1)
size = len(list1)
def binary_search(x):
    print("BINARY SEARCHING")
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if list1[mid] < x: 
            low = mid + 1
        elif list1[mid] > x: 
            high = mid - 1
        else: 
            return mid 
    return -1

def lsearching(n):
	print("LINEAR SEARCHING")
	if n not in list1:
		print(n,"not in the list")
	else:
		for i in range(size):
			if list1[i]==n:
				print("index of ", n," is ",i)
				
n = input("Enter (L) for Linear search and  (B) for Binary search \n ")
if n=="L" or n=="l":
	v = int(input("Enter a no. from the list1 "))
	lsearching(v)
elif n=="B" or n=="b":
	v = int(input("Enter a no. from the list1 "))
	print("index of ",v," is ",binary_search(v))
else:
	print("Invalid input")
