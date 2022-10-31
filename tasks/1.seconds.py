#Declare the time as a list 
Time = [0,0,0]
#allows you to input 3 different time values with  colon seperating them
Time = (input("Please input a time")).split(":")
#does the calculations and outputs the time
print((int(Time[0]) * 3600) + (int(Time[1]) * 60) + int(Time[2]))

