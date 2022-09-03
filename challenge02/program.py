import sys
def is_valid_tag(input_string):
    stack = []

    for i, char in enumerate(input_string):
        if char == '<':

            # index of '<' and '>' respectively
            open_index = i
            closed_index = input_string.find('>', open_index)
            # if the character after the '<' is a '/' (represents closing tag)
            if input_string[open_index + 1] == '/':

                # if stack is not empty and the top of the stack is equal to the the contents inside <...>
                if stack and stack[-1] == input_string[open_index + 2:closed_index]:
                    stack.pop()
                else:
                    return 'Unbalanced'
            else:

                # the tag is an opening tag
                # add the string inside < > to the stack 
                stack.append(input_string[open_index+1:closed_index])

            # sliding window ensures algorithm is O(n)
            i = closed_index

    return 'Balanced' if not stack else 'Unbalanced'

def main():
    for line in sys.stdin:
        print(is_valid_tag(line))
        
if __name__ == '__main__':
    main()