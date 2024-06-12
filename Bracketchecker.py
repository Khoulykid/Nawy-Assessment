#Assuming empty string is also valid
def isValid(s): 
    if(s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}')):
        return False
    flag = -1
    for i in range(len(s)):
        if (s[i] == '('):
            flag = 0
        elif (s[i] == '['):
            flag = 1
        elif (s[i] == '{'):
            flag = 2

        if (s[i] == ')' and flag != 0):
            return False
        elif (s[i] == ']' and flag != 1):
            return False
        elif (s[i] == '}' and flag != 2):
            return False
    return True

print(isValid("()"))