import sys
def isValidTag(s):
    stack = []

    for i, char in enumerate(s):
        if char == '<':

            # index of '<' and '>' respectively
            openIndex = i
            closedIndex = s.find('>', openIndex)
            
            # if the character after the '<' is a '/' (represents closing tag)
            if s[openIndex + 1] == '/':

                # if stack is not empty and the top of the stack is equal to the the contents inside <...>
                if stack and stack[-1] == s[openIndex + 2:closedIndex]:
                    stack.pop()
                else:
                    return 'Unbalanced'
            else:

                # the tag is an opening tag
                # add the string inside < > to the stack 
                stack.append(s[openIndex+1:closedIndex])

            # sliding window ensures algorithm is O(n)
            i = closedIndex

    return 'Balanced' if not stack else 'Unbalanced'

def main():
    for line in sys.stdin:
        print(isValidTag(line))
        
if __name__ == '__main__':
    main()