import sys

def evaluate_boolean_equation(boolean_equation):
    # Implementing a stack to evaluate the boolean equation
    stack = []
    for char in boolean_equation:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Evaluate the expression inside the parentheses
            while stack[-1] != '(':
                operand2 = stack.pop()
                operator = stack.pop()
                operand1 = stack.pop()
                if operator == '+':
                    stack.append(operand1 or operand2)
                elif operator == '*':
                    stack.append(operand1 and operand2)
            stack.pop() # Remove the opening parenthesis
        elif char in ['+', '*']:
            stack.append(char)
        else:
            # Convert the variable to a boolean value
            stack.append(True if char == '1' else False)
    # Evaluate the remaining expression
    while len(stack) > 1:
        operand2 = stack.pop()
        operator = stack.pop()
        operand1 = stack.pop()
        if operator == '+':
            stack.append(operand1 or operand2)
        elif operator == '*':
            stack.append(operand1 and operand2)
    return stack[0]

if __name__ == '__main__':
    
    boolean_equation = input('What is the boolean equation?')
    result = evaluate_boolean_equation(boolean_equation)
    #ask for commands for what to do to boolean equation
    print(boolean_equation)
