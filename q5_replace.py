# 5. Replace a given character with ’*’ Given a string, and a character to replace,
# return a string where each occurance of the character is replaced with ’*’.

# takes in sentence, old char, new character
def replaceChar(sentence, old, new):
    # check if the sentence is empty
    if sentence == '':
        return ''
    # if the sentence array contains old, return new char and continue recursion    
    if sentence[0] == old:
        return new + replaceChar(sentence[1:], old, new)
    return sentence[0] + replaceChar(sentence[1:], old, new)

# sentence
sentence = "Hello world"

#old character
old = 'o'
# new character
new = '*'

# print and call function
print(replaceChar("Hello world", 'o', '*'))
