import re

def solve(s):
    result = ''
    for i in s[:].split(' ', -1):
        if ('' == i):
            result += (' ')
        elif(re.match('^[a-zA-Z]$', i[0])):
            result += (i.capitalize() + " ")
        else:
            result += (i + " ")
    return result


print(solve("1 2  3"))
print(solve("bakkesh aladahalli"))
