def is_balanced(expression):
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to match closing brackets to opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}

    # Traverse each character in the expression
    for char in expression:
        # If it's an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)

        # If it's a closing bracket
        elif char in bracket_map.keys():
            # Stack must not be empty and the top element should match the current closing bracket
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False

    # If the stack is empty, all opening brackets have been matched
    return len(stack) == 0


# Get the expression input from the user
user_expression = input("Enter an expression: ")

# Check if the parentheses are balanced
if is_balanced(user_expression):
    print("The expression has balanced parentheses.")
else:
    print("The expression does not have balanced parentheses.")
