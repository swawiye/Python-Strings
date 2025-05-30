# 1. Print the number of words in a sentence
sentence = "Welcome to Python Programming!"
numberOfWords = len(sentence.split()) # "split" counts the number of words in the sentence
print(f"The number of words in the sentence are: {numberOfWords}")

# 2. Checking if two strings are anagrams of each other
# Anagram -a word, phrase, or name formed by rearranging the letters of another; ex listen and silent
# Using sorted
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2): # checks if the sorted characters are the same
    print(f"Yes, {str1} and {str2} are anagrams of each other")
else:
    print(f"No, {str1} and {str2} are not anagrams of each other")

# Using user input
s1 = input("Enter a word: ")
s2 = input("Enter another word: ")

def anagrams(s1, s2):
    # Remove spaces(ex: dirty room and dormitory) and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

if anagrams(s1, s2):
    print(f"{s1} and {s2} are anagrams of each other")
else:
    print(f"{s1} and {s2} are not anagrams of each other")

# 3. Checking if an input string is a palindrome
# Palindrome -a word, phrase, or sequence that reads the same backwards as forwards, ex; madam, nurses run
# Using slicing
str = "madam" # racecar, abba

if str == str[::-1]: # 's[::-1]'(regular expression) reverses the string and compares it to the original
    print("Yes")
else:
    print("No")  

#def isPalindrome(str):
#    lastIndex = len(str)-1
#    line = len(str)//2
#    for i in range(0, line):
#        if str[1] != str[lastIndex-1]:
#            return False
#    return True