num = int(0)
while num > 3 or num < 1 : #question is asked until the correct numbers are input
    num = int(input('Please enter a number between 1 and 3'))
    #endwhile
print("Your number is " + str(num))