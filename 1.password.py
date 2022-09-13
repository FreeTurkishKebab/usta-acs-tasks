
from ast import If
password = input("Please enter a password: ") #prompts password entry

if len(password)<6:  #checks whether the password is under 6 digits
  print('password is invalid')
if len(password)>=6:
 print('password is valid') #valid and invalid printed depending on length