list1 = [1,5,7,18,20,22]
list2= [6,13,21,24]
mergeList = []
length = len(list1) + len(list2)
length = length - 1

a = 0
while a <= length : 
    mergeList.append(a)
    a = a + 1

i = 0 
g = 0 
k = 0
while i <= length :
    if list1[g] <= list2[k] :
        mergeList[i] = list1[g]
        g = g + 1
        i = i + 1
    else :
        mergeList[i] = list2[k]
        k = k + 1
        i = i + 1

z = 0 
while z <= length :
    print(mergeList[z])
    z = z + 1

