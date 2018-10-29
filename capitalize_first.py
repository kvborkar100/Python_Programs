# Using the Python language, have the function LetterCapitalize(str) take the str parameter 
# being passed and capitalize the first letter of each word. 
# Words will be separated by only one space.


def capitalize(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    print(' '.join(words))

str = input("Enter string to Capitalize: ")
capitalize(str)