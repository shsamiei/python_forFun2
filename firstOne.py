
numberOf_employees = int(input())
dict = {}

for i in range(numberOf_employees) :
    string = input().split()
    if string[0] in dict :
        dict[string[0]] += 1 
    else :
        dict[string[0]] = 1  


max  = 0 

myvalueList = list(dict.values())

for i in range(len(dict.values())) :
    if myvalueList[i] > max :
        max = myvalueList[i]


print(max)


