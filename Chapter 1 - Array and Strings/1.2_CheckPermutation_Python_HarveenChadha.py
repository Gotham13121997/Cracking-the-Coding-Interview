# your code goes here
# your code goes here

# 1.2 Check Permutation
# online Link - https://ideone.com/B7tEGE
string1 = input("Please enter string 1\n")
string2 = input("Please enter string 2\n")

def CheckString(input):
	dict ={}
	for i in range(len(input)):
		if input[i] not in dict:
			dict[input[i]] = 1
		else:
			dict[input[i]] += 1
	return dict

if len(string1) != len(string2):
	print("Certainly not a permutation")
else:
	dict1 = CheckString(string1)
	dict2 = CheckString(string2)
	flag=0	
	
	
	for key in dict1:
		
		if key in dict2:
			
			if dict2[key] != dict1[key]:
			
				flag=1
				break
		else:
			flag=1
			break
if flag==1:
	print("Not a permutation")
else:
	print("Permutation")
