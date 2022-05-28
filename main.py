# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
#Name: Osarenkhoe Chima-Nwogwugwu
#Student ID: I4G033993TR5

def find_anagram(word, anagram):
 
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        return True
    else:
        return False
print(find_anagram("race", "care"))

