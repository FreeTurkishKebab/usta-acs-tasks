list = [38,328,53,24,15,78,23,99,29,6,3,7,44,94,75,23,]
for i in range (0, (len(list) - 2)):
    for j in range (0, (len(list) - i - 1)):
        if list[j] > list[j + 1]:
             c = list[j]
             c2 = list[j + 1]
             list[j] = c2
             list[j + 1] = c

print(list)