# Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet 
# (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def letter_change(s):
    letters = list(s)
    for i in range(len(letters)):
        if letters[i] == 'Z' or letters[i] == 'z':
            letters[i] = 'A'
        else:
            letters[i] = chr(ord(letters[i]) + 1)
    
    for i in range(len(letters)):
        if letters[i] in ('a', 'i', 'o', 'e', 'u'):
            letters[i] = letters[i].upper()
            
    print("New String is: {}".format(''.join(letters)))

if __name__ == "__main__":
    str = input("Enter a word: ")
    letter_change(str)