# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from typing import List

# class Student(object):
# 	def __init__(self, aFirstnam, aAge, aLastname):
# 		self._firstname = firstnam
# 		self._lastname = lastname
# 		self._age = age

# 	def display(self):
# 		pass

# file_path = "new_directory/new_file.txt"
# # Open the file in write mode ("w")
# with open(file_path, "w") as file:
#     file.write("This is a new file created by Python.")

# print("File created and written successfully.")


import os

# Check if a file exists
file_path = "my_file.txt"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")

# Delete a file
file_to_delete = "file_to_delete.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted.")
else:
    print("File not found.")

# Rename a file
old_name = "old_name.txt"
new_name = "new_name.txt"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed.")
else:
    print("File to rename not found.")

# List directory contents
directory = "my_directory"
if os.path.exists(directory):
    contents = os.listdir(directory)
    print("Directory contents:", contents)
else:
    print("Directory not found.")
