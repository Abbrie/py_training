trainees=["john",[2, ["James","Mary"]]]
print(trainees[1][1][1])
#output James from list
print(trainees[1][1][0])
#Using a methodadd 56 at the end of the list
trainees.append(56)
print(trainees)
#Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,"Mike")
print(trainees)
#Change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#Remove John and Mary from the list



#Using a function,determine the length of the list
length=len(trainees)
#print(length)