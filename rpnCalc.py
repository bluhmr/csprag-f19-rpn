
import operator

operators = {
        '+': operator.add,
        '-': operator.sub,
	'*': operator.mul,
	'/': operator.floordiv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

    return stack.pop()



while True:
	result = calculate(input('rpnCalc> '))
	print(result)

