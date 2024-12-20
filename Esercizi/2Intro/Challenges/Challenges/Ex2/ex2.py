# Define a simple calculator.
# The user uses the terminal and it has three variables.
#  - input1: first integer number
#  - input2: second integer number
#  - type of operation: a number associated to the operation
#     (e.g., 0 for the addition)

inp1 = input('Enter int input1: ')
inp2 = input('Enter int input2: ')
operation = input('Enter operation: ')
res = 0

match operation:
    case '0':
        res = int(inp1) + int(inp2)
    case '1':
        res = int(inp1) - int(inp2)
    case '2':
        res = int(inp1) * int(inp2)
    case '3':
        res = int(inp1) / int(inp2)

print(res)
