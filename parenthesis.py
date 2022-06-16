def parethesis_validator(s):
    if len(s) % 2 == 1:
        return False
    
    paren = {')': '(', 
            '}' : '{', 
            ']' : '['}
    stack = []
    for i in s:
        if i not in paren:
            # keep adding opening parenthesis to the stack
            stack.append(i)
            
        else:
            # if i not and opening bracket then 'i' is a closing bracket
            # check if the last charctoer is a matching 'i'
            if stack and stack[-1] == paren[i]:
                stack.pop()
            else:
                # it a bad match, return false , example "}"  != "["
                return False
    # return if stack is empty meaning all open bracket have closing brac..t
    # else False meaning stack is not empty : ex: s = "{{()"
    return not stack

def main():
    s = "{}[](()))"
    print(parethesis_validator(s))
    return 0 

main()