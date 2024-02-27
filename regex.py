# #  This search for a singel parttern within the string.
# # import re

# # txt = "The rain in Spain"
# # pattern = r".*rain.*"
# # match = re.search(pattern, txt)

# # if match:
# #     print("Pattern found!")
# # else:
# #     print("Pattern not found!")

# # # This search for multiple  partterns within the string. 
# # import re

# # txt = "The quick brown fox jumps over the lazy dog"
# # pattern = r".*(fox|dog).*"
# # match = re.search(pattern, txt)
# # if match:
# #     print("Pattern found!")
# # else:
# #     print("Pattern not found!")

# # import re     
# # r = "the book  has a brook in the hood"
# # t = re.split("\s", r, 3)
# # print(t)


# # import re

# # txt = "The rain in Spain,is an amazing grace"
# # x = re.sub(r"\s", " ", txt)
# # print(x)

# # if x == t:
# #     print("Right whitespace")
# # else:
# #     txt = "The rain in Spain,is an amazing grace"
# #     x = re.search(r"rain$", txt)
# #     print(x)
 
# import re  
# rep= "Coding if fun,fun!,fun but hard!!! "
# code = re.sub("hard", "hard", rep)
# print(code)
# rode = "You need the knoledge of substitution"
# if code == code:
#     print("You are right about coding")
# else :
#     print("Its just the opposite of it all")
    
#     import re

# txt = "The cat and the dog are friends"
# patterns = [r"cat", r"dog"]
# replacements = ["tiger", "wolf"]

# new_txt = re.sub("|".join(patterns), lambda m: replacements[patterns.index(m.group(0))], txt)
# print(new_txt)

# #list comprehension in python 
# txt = [1, 34, 5, 67, 78, 8]
# x = [9 if element == 5 else element for element in txt]
# print(x)
# #  search for multiplecharacter
# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())

# #  printing of multiple characters:
# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# if x:
#     print(x.group())  # Print the matched word
# else:
#     print("No match found")

# #  change the lowercase "s" character to uppercase
# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# if x:
#     matched_word = x.group()
#     capitalized_word = matched_word.replace(matched_word[0], matched_word[0].upper())
#     print(capitalized_word)  # Print the capitalized word
# else:
#     print("No match found")


# # handle characters other than "S" and 
# # capitalize them if found at the beginning of a word, you can make the following changes:
# import re

# txt = "The rain in Spain"
# x = re.search(r"\b(\w)\w+", txt)
# if x:
#     matched_word = x.group()
#     capitalized_word = matched_word.replace(matched_word[0], matched_word[0].upper())
#     print(capitalized_word)  # Print the capitalized word
# else:
#     print("No match found")


# # To handle characters other than "S" at the
# # beginning of a word and capitalize them

# import re

# txt = "The rain in Spain"
# x = re.search(r"\b(\w)\w+", txt)
# if x:
#     matched_word = x.group()
#     first_char = matched_word[0]
#     capitalized_word = matched_word.replace(first_char, first_char.upper())
#     print(capitalized_word)  # Print the capitalized word
# else:
#     print("No match found")


import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
