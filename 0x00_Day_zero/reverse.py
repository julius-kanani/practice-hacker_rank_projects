# -*- coding: utf-8 -*-
"""
Spyder Editor

This python script reverses alphabetic characters only in a string leaving out
special characters e.g., [!@#$%^&*()_+=,.].
"""

string = "a-y%^f**k$you&"
# Reverse the list for alphanumeric characters only.
list = [char for char in string[::-1] if char.isalpha()]

# Insert the special characters left out to the list
for index, char in enumerate(string):
    if not char.isalpha():
        list.insert(index, char)
        
# join the result to a word
result = "".join(list)

# print the result
print(result)