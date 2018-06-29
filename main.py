#!/usr/bin/env python

import sys

PRECEDENCE = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}


class Calculator(object):

    variables = {}

    def calc(self, input_str):
        return(self._postfix_eval(self._infix_to_postfix(input_str)))

    def calc_with_vars(self, input_list):
        results_list = []
        for equation in input_list:
            [name, expression] = equation.split(" = ")
            value = self._postfix_eval(self._infix_to_postfix(expression))
            self._save_variable(name, value)
            results_list.append(value)
        return(results_list)

    def _save_variable(self, name, value):
        self.variables[name] = value

    def _should_continue(self, op_stack, token):
        if not op_stack.isEmpty():
            if token in self.variables.keys():
                return(True)
            elif PRECEDENCE[op_stack.peek()] >= PRECEDENCE[token]:
                return(True)
        return(False)

    def _numeric_token(self, token):
        try:
            float(token)
        except:
            return(False)
        return(True)

    def _infix_to_postfix(self, infix_expression):
        op_stack = Stack()
        postfix_list = []
        token_list = infix_expression.split()
        for token in token_list:
            if self._numeric_token(token):
                postfix_list.append(token)
            elif token in self.variables.keys():
                postfix_list.append(str(self.variables[token]))
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                while (self._should_continue(op_stack, token)):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.isEmpty():
            postfix_list.append(op_stack.pop())

        return(" ".join(postfix_list))

    def _postfix_eval(self, postfixExpr):
        operandStack = Stack()
        tokenList = postfixExpr.split()
        for token in tokenList:
            if self._numeric_token(token):
                operandStack.push(float(token))
            elif token in self.variables.keys():
                operandStack.push(float(self.variables[token]))
            else:
                operand_2 = operandStack.pop()
                operand_1 = operandStack.pop()
                result = apply_operation(token, operand_1, operand_2)
                operandStack.push(result)
        return(operandStack.pop())


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return(self.items == [])

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[len(self.items)-1])

    def size(self):
        return(len(self.items))

    def print_stack(self):
        print(self.items)


def apply_operation(operation, operand_1, operand_2):
    if operation == "*":
        return operand_1 * operand_2
    elif operation == "/":
        return operand_1 / operand_2
    elif operation == "+":
        return operand_1 + operand_2
    else:
        return operand_1 - operand_2


def main(argv):
    calculator = Calculator()

    print "First Step"  # 5.857142
    print calculator.calc("3.0 + 4 * 5 / 7")

    print "\nSecond Step"  # 5.0
    print calculator.calc("( 3.0 + 4 ) * 5 / 7")

    print "\nThird Step"  # [3, 243]
    print calculator.calc_with_vars([
        "pi = 3",
        "pizza = 9 * 9 * pi"
    ])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
