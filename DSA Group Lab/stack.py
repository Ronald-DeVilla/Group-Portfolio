def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):
        return 3
    return 0

def infix_to_postfix_conversion(infix):
    stack = []
    postfix = ''
    steps = []

    for char in infix:
        if char.isalnum():
            postfix += char
            steps.append(postfix)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
                steps.append(postfix)
            stack.pop()
        elif char in '+-*/^':
            while stack and stack[-1] not in '()' and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
                steps.append(postfix)
            stack.append(char)

    while stack:
        postfix += stack.pop()
        steps.append(postfix)

    return postfix, steps