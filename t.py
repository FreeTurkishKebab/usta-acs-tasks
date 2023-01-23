list = ["Sophie","Lily","Jessica","Isabella","Ava","Poppy","Emily","Isla","Olivia","Amelia"]
for i in range (0, (len(list) - 2)):
    for j in range (0, (len(list) - i - 1)):
        if list[j] > list[j + 1]:
             c = list[j]
             c2 = list[j + 1]
             list[j] = c2
             list[j + 1] = c
    print(list)
