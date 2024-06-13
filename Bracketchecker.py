#Assuming empty string is also valid
def isValid(s): 
    if(s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}')):
        return False
    maps = []
    for i in range(len(s)):
        if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
            maps.append(s[i])
    for i in range(len(s)):
        if (s[i] == ')' and maps[len(maps)-1] != '('):
            return False
        elif (s[i] == ']' and maps[len(maps)-1] != '['):
            return False
        elif (s[i] == '}' and maps[len(maps)-1] != '{'):
            return False
        maps.pop()
    return True

print(isValid("()"))