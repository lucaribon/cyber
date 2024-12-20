# You are asked to define a Python code that, given a string,
# prints a string with all of the letters shifted by 2.
#
# For example,
# input = 'abc'
# otput = 'cde'

alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inp = input('Enter a string: ')
res = ""

for letter in inp:
    index = alphabet.index(letter)
    res += alphabet[(index + 2) % 26]

print(res)
