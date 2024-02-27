# username = input("Enter username: ")
# age = int(input("User age is: "))  # Convert the input to an integer
# info = "The username is " + username + " and age is " + str(age)  # Convert age to string for concatenation

# while age == 53:
#     print('Please enter the right age')
#     age = int(input("User age is: "))  # Prompt user for age again

# print(info)


username = input("Enter username: ")
age = int(input("User age is: "))  # Convert the input to an integer
info = "The username is " + username + " and age is " + str(age)  # Convert age to string for concatenation

while age < 50 or age > 60:
    print('Please enter an age between 50 and 60')
    age = int(input("User age is: "))  # Prompt user for age again

print(info)

