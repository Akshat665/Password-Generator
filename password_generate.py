import random
import string
length = int(input("Enter the length of the password : "))
pass_type = input("What should be the type of password(write (a) for all types i.e, password,(n) for Numerical password and (l) for letter only password : ")


while length == "":
 print("You haven't entered the length of the password")
 length = int(input("Enter the length of the password : "))

while pass_type == "":
    print("You haven't enetered the type of password")
    pass_type = input("What should be the type of password(write (a) for all types i.e, password,(n) for Numerical password and (l) for letter only password: ")


if pass_type.lower() == 'n':
  numerical_result = "".join(random.choice(string.digit) for _ in range (length))
  print(f"Here's your password {numerical_result} ")

if pass_type.lower() == 'l':
  ascii_result = "".join(random.choice(string.ascii_letters) for _ in range (length))
  print(f"Here's your password {ascii_result} ")

if pass_type.lower() == 'a':
 char = string.ascii_letters + string.digits
 char_result = "".join(random.choice(char) for _ in range (length))
 print(f"Here's your password {char_result} ")






