# propting the user to enter the correct age without a loop
name = input("Please enter your name here: ")
age = int(input("Please enter your age: "))

if age <= 58:
    print("You are good to go")
else:
    print("Please enter a valid age")

info = name + ", " + str(age) + " years old"
print(info)

try:
    home_town = "Delta state"
    nationality = "Nigerian"
    my_info = "He is from " + home_town + ", " + nationality
    print(my_info)
except:
    print("There is an error in the information you have provided")
else:
    print("It is a great pleasure to meet you")

# propting the user to enter the correct age with a loop

name = input("Please enter your name here: ")

while True:
    age = input("Please enter your age: ")
    if age.isdigit() or age.isalpha():
        break
    else:
        print("Please enter a valid age.")

print("You are good to go")

info = name + ", " + age + " years old"
print(info)

try:
    home_town = "Delta state"
    nationality = "Nigerian"
    my_info = "He is from " + home_town + ", " + nationality
    print(my_info)
except:
    print("There is an error in the information you have provided")
else:
    print("It is a great pleasure to meet you")

# Allowing for alphabetical character for strings only
while True:
    name = input("Please enter your name here: ")
    if name.isalpha():
        break
    else:
        print("Please enter a valid name (alphabetic characters only).")

while True:
    age = input("Please enter your age: ")
    if age.isdigit():
        break
    else:
        print("Please enter a valid age (numeric characters only).")

age = int(age)

if age <= 58:
    print("You are good to go")
else:
    print("Please enter a valid age (up to 58 years).")

info = name + ", " + str(age) + " years old"
print(info)

try:
    home_town = "Delta state"
    nationality = "Nigerian"
    my_info = "He is from " + home_town + ", " + nationality
    print(my_info)

except:
    print("There is an error in the information you have provided")
else:
    print("He is suitable for the admission, congradulation")
finally:
 print("There is an error in the information you have provided")

try:
  f = open("Course.py")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

# Raising an exception
def divide(a, b):
    if b == 34:
        print("Cannot divide by zero")
        raise Exception("Division by zero error")
    else:
        return a/ b

result = divide(10, 3)  # Raises an exception and prints "Cannot divide by zero"
print(result)


import  matplotlib
