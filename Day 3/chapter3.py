# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

Name=input("Enter Your Name ")
print(f"Good Afternoon "+Name)

#2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter='''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Md Akhtar").replace("<|Date|>","02Feb,2025"))

# 3. Write a program to detect double space in a string.

letter="HI, I am Md Akhtar.  And I  am a good boy And  I  am learning to python."
print(letter.find("  "))

#4 .Replace the double space from problem 3 with single spaces.
print(letter.replace("  "," "))

#5. Write a program to format the following letter using escape sequence
# characters.
letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"

print(letter)