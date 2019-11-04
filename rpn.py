#!/usr/bin/env python3

import operator

import sys

#from termcolor import colored


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '>>': operator.lshift,
    '<<': operator.rshift,
    '|': operator.or_,
    '&': operator.and_,

}

def calculate(myarg):
    stack = list()
    #for token in myarg.split():
     #   try:
      #      token = int(token)
       #     if (token > 0):
        #        print(colored(token, 'green'), end = ' ')
         #   elif (token < 0):
          #      print(colored(token, 'red', attrs=['bold']), end = ' ')
           # else:
            #    print(colored(token, 'blue'), end = ' ')
        #except ValueError:
         #   print(colored(token, 'magenta', attrs=['blink', 'bold', 'dark']))
            
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        #if (result < 0):
         #   print(colored(result, 'red', attrs=['bold']))
        #elif (result > 0):
         #   print(colored(result, 'green'))
        #else:
         #   print(colored(result, 'blue'))
        print(result)

if __name__ == '__main__':
    main()
