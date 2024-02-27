x = pow(4, 3)
print(x)
y = pow(6,6)
print(y)
t = pow(5,7)
if t < 5:
 print("You now have a score")
elif  t > 48:   
 print("Check your score to be sure")
 print (t)
 
 
 def encrypt(message, public_key):
    encrypted_message = pow(message, public_key[0], public_key[1])
    return encrypted_message

def decrypt(encrypted_message, private_key):
    decrypted_message = pow(encrypted_message, private_key[0], private_key[1])
    return decrypted_message

# Example usage
message = 42
public_key = (13, 77)  # Public key (exponent, modulus)
private_key = (37, 77)  # Private key (exponent, modulus)

# Encryption
encrypted = encrypt(message, public_key)
print("Encrypted:", encrypted)

# Decryption
decrypted = decrypt(encrypted, private_key)
print("Decrypted:", decrypted)
def sum_numbers(a, b):
    sum = a + b
    return sum

result = sum_numbers(3, 4)
print(result)  # Output: 7
import math
X =  math.sqrt(2)
print(X)
if X >  489: 
 print("You are lieing about this figures")
else :
 print("Correct Math guru")
 
 
import json

data = {
    "name": ["John Doe", "James", "Ruth"],
    "age": None ,
    "is_student": True,
    "courses": ["Math", "Science", "History"]
}

# Accessing individual names in the "name" list
for name in data["name"]:
    print(name)

# Removing "Ruth" from the "name" list
data["name"].remove("Ruth")

# Serialize the modified data to a JSON string
json_data = json.dumps(data,indent= 1)
print(data)


import json

json_data = '{"name": "John Doe", "age": 30, "is_student": true, "courses": ["Math", "Science", "History"]}'
data = json.loads(json_data)
fammated_int = json.dumps(data,indent=23)
print (fammated_int)


their_names = '{}' " , {}"
whoare_they = "Are the two young individauls from lagos Nigeria"
final_info = their_names,  +  whoare_they
final_info.format( "joshua", "Mainad")
print(final_info)