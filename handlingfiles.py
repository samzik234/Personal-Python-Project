# f = open("\Users\Azike ", "w")
# f.write("love coding")
# f.close()

# f = open("Desktop\word.txt", "r")
# print(f.read())
# f.close()



import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", Users\Azike Simon Shinye\Desktop)

# Construct the full path to a file or directory
file_path = os.path.join(Desktop, "file.txt")
directory_path = os.path.join(Desktop, "my_directory")

print("File Path:", file_path)
print("Directory Path:", directory_path)


# Get the current working directory
current_directory = os.getcwd()

# Specify the file path for the new file in the current directory
file_path = os.path.join(Desktop, "new_file.txt")

# Open the file in write mode ("w")
with open(file_path, "w") as file:
    # Write content to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")
