# @author: vinay
# Checking for incomplete parenthesis in a string
def checkparen(inpExpn):
    stack = []
    idxstack = []
    i = 0
    for x in inpExpn:
        #print('DEBUG: x = ' + str(x))
        
        if (x == '('):
            stack.append(x)
            idxstack.append(i)
        elif (x == ')'):
            if len(stack) !=0:
                if stack[-1] == '(':
                    stack.pop()
                    idxstack.pop()
                else:
                    return str(idxstack[-1])
            elif len(stack) ==0:
                return str(i)
        elif (x == '['):
            stack.append(x)
            idxstack.append(i)
        elif (x == ']'):
            if len(stack) !=0:
                if stack[-1] == '[':
                    stack.pop()
                    idxstack.pop()
                else:
                    return str(idxstack[-1])
            elif len(stack) == 0:
                return str(i)
        
        i = i + 1
        #print('DEBUG: ' + str(stack) + str(idxstack))
    if (len(stack) == 0):
        return 'match'
    else:
        if len(stack) !=0:
            return str(idxstack[0])

x = 'a+b(c+d)'
print(x,'position of mismatch or match:', checkparen(x))
x = 'a+b+[(c+d)(e+f)'
print(x,'position of mismatch or match:', checkparen(x))
x = '34(12+5))'
print(x,'position of mismatch or match:', checkparen(x))
x = '34(12+5'
print(x,'position of mismatch or match:', checkparen(x))
x = '34)12+5('
print(x,'position of mismatch or match:', checkparen(x))
x = 'a+b+[((a+b).(a+b))+(a+b]'
print(x,'position of mismatch or match:', checkparen(x))