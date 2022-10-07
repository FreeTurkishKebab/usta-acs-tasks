Mylist = [0,0,0,0,0,0]
i = 0 
num = int(input("How many students would you like to input"))
while i < num :
    Mylist[i] = input()
    i = i + 1
name = input("Please enter a name")
i = 0 
while i < num : 
    if name == Mylist[i] : 
        print("The student record number is: ", (i + 1))
        i = num + 1
    else :
        i = i + 1

        
    
