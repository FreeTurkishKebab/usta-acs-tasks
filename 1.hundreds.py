num = int(0)
while num < 100 or num > 999 : #a loop to make sure right number is entered
  num = int(input("Please input a number between 100 and 999")) 
#endwhile 
hundred = num // 100 #we calculate the hundred value
fakehundred = hundred * 100  #we use a rounded down hundred value to calculate the ten
realten = num - fakehundred 
ten = realten // 10 #we finally obtain the actual ten value 
faketen = ten * 10 #we calculate a rounded down ten value to find the unit 
fakeunit = faketen + fakehundred
unit = num - fakeunit #we obtain the final unit 
print("The hundred value is" + str(hundred) + ",the ten value is" + str(ten) + "and the unit is" + str(unit))