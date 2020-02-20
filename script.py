import sys
num = list(sys.argv[1])
sum = 0
tempsum = 0
newl = []
newimei = []
for i in range(0,15):
	if(i%2 == 0):
		newl.append(int(num[i]))
	else:
		if(int(num[i])*2 >= 10):
			tempnum = int(num[i])*2
			tempsum = 0
			tempsum = tempnum%10
			tempnum = int(tempnum/10)
			tempsum += tempnum%10
			newl.append(tempsum)
		else:

			newl.append(int(num[i])*2)
for i in range(0,15):
	sum += int(newl[i])
if(sum%10 == 0):
	print("Valid IMEI")
	newimei = num
	strimei = ""
	while((int(newimei[14])) < 9 and (int(newimei[12])) > 0):
		newimei[14] = int(newimei[14])+1
		newimei[12] = int(newimei[12])-1
		for j in range(0,15):
			strimei += str(newimei[j])
		print(strimei)
		strimei=""
	strimei=""
	newimei = num
	while((int(newimei[14])) > 0 and (int(newimei[12])) < 9):
		newimei[14] = int(newimei[14])-1
		newimei[12] = int(newimei[12])+1
		for j in range(0,15):
			strimei += str(newimei[j])
		print(strimei)
		strimei=""
	strimei = ""
	newimei = num
	while((int(newimei[13])) < 9 and (int(newimei[11])) > 0):
		newimei[13] = int(newimei[13])+1
		newimei[11] = int(newimei[11])-1
		for j in range(0,15):
			strimei += str(newimei[j])
		print(strimei)
		strimei=""
	strimei=""
	newimei = num
	while((int(newimei[13])) > 0 and (int(newimei[11])) < 9):
		newimei[13] = int(newimei[13])-1
		newimei[11] = int(newimei[11])+1
		for j in range(0,15):
			strimei += str(newimei[j])
		print(strimei)
		strimei=""
else:
	print("The IMEI is Invalid!!!!!!!1")
	print(sum)
	print(newl)
