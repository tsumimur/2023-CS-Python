from operator import add, mul, sub, truediv
from typing import List, Optional, Union

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def prefix_evaluate(prefix_evaluation: str) -> int: 
    stack = []

    if prefix_evaluation == "":
        return None
    
    for token in reversed(prefix_evaluation.split()):
        if token.isdigit():
            stack.append(int(token))
        else:
            if token in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()

                result = ops[token](op1, op2)
                
                stack.append(result)

    return stack[0]


def to_prefix(equation: str) -> str:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    operators = set("+*-/")
    output = []
    stack = []

    for token in reversed(equation.split()):
        if token.isdigit():
            output.append(token)
        elif token in operators:
            while stack and stack[-1] != ")" and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == ")":
            stack.append(token)
        elif token == "(":
            while stack and stack[-1] != ")":
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return " ".join(list(reversed(output)))


def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
