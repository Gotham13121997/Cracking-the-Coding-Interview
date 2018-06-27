

# Problem 1.1 IsUnique
# Online Link- https://ideone.com/V2m9I5


# When You can use another datastrucure

a = input("Please enter your input:\n") 
dict = []
flag =0
for i in range(len(a)):
	if a[i] in dict:
		flag=1
		break
	else:
		dict.append(a[i])
if flag==1:
	print("Not unique")
else:
	print("Unique")
	
# Part 2: When you cannot use any other datastructure

for i in range(len(a)):
	for j in range(i+1,len(a)):
		if(a[j] == a[i]):
			flag=1
			break
if flag==1:
	print("Not unique")
else:
	print("Unique")		
	
