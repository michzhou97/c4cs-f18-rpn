#!/usr/bin/env python3

import operator
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '!': math.factorial,
}

def calculate(myarg, hist):
    stack = list()
    if myarg == "history":
        answer = hist.pop()
        op = hist.pop()
        if op == '!':
            arg1  = hist.pop()
            
            return "{arg1} ! = {answer}".format(answer=answer, arg1=arg1)
        else:
            arg2 = hist.pop()
            arg1 = hist.pop()

            return "{arg1} {op} {arg2} = {answer}".format(arg1=arg1, op=op, arg2=arg2, answer=answer)
    else:
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                function = operators[token]
                if token != '!':
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    if token == '/' and arg2 == 0:
                        return "Divide by zero error"
                    hist.append(arg1)
                    hist.append(arg2)
                    hist.append(token)
                    result = function(arg1, arg2)
                    stack.append(result)
                    hist.append(result)
                else:
                    arg1 = stack.pop()
                    hist.append(arg1)
                    hist.append(token)
                    result = function(arg1)
                    stack.append(result)
                    hist.append(result)
                print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    hist = list()

    while True:
        result = calculate(input("rpn calc> "), hist)
        print("Result: ", result)

if __name__ == '__main__':
    main()
