def longestWord(s):
    words = s.split()
    max = 1
    long_word = words[0]
    for i in words:
        len_s = len(i)
        if len_s > max:
            max = len_s
            long_word = i
    return long_word

if __name__ == "__main__":
    str = input("Enter the string: ")
    print("Longest Word in the string is: {}".format(longestWord(str)))


                                                                        