myString = input("Please input a string to test")
Answer = False 
letters = [myString]
numChars = list(letters)
numChars = letters[0 : len(myString)]
reverse = []
x = 0 
while x < (len(myString)-1) :
    reverse[x] = reverse[(len(myString)-1)]
    x = x + 1
print(numChars)