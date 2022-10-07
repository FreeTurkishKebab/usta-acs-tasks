#asks the user for all three of input values
num1 = int(input("Please enter number 1"))
num2 = int(input("Please enter number 2"))
num3 = int(input("Please enter number 3"))
#the biggest number is decided by the max and the smallest by min 
a = max(num1 , num2 , num3)
c = min(num1 , num2 , num3)
b = ((num1 + num2 + num3) - (a + c))
#the middle number is decided by addition of all 3 minus "a" and "c"
print(a , b ,c)
    #prints whichever one is bigger first followed by the middle and smallest
#end if