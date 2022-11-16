from collections import deque

def brackets(line):
    stack = deque()
    for i in line:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

    
print(brackets("(()())"))
# 0
print(brackets(""))
# 0
print(brackets("(()()))"))
# -1
print(brackets(")()())("))