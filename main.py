import string
#Cleaning Text Steps
# 1) Create a text file and take text from it

text = open("read.txt", encoding='utf-8').read()
#print(text)

# 2) convert letter into lowercase ('Enim')

lower_case = text.lower()
#print(lower_case)

# 3) Remove punctuations like ,:;/!

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
""" 
str1 : Specifies the list of characters that need to be replaced.
str2 : Specifies the list of characters with which the characters need to be replaced.
str3 : Specifies the list of characters that needs to be deleted.
"""
print(cleaned_text)