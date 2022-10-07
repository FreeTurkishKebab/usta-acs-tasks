#get a number to be input 
num = int(input("Please input a number"))
i = 1 
#create a while loop to find all factors
while i <= num : 
    #create an if statement to make sure the remainder is 0 and it is a factor 
    if int(num % i) == 0 :
        print(i)
    i = i + 1