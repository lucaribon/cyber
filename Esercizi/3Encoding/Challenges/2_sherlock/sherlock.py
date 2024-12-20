import binascii

string = ""

with open("challenge.txt") as f:
    for line in f:
        for c in line:
            if c.isupper():
                string += c

print(string)

binary = ""
temp = ""
for c in string:
    temp += c
    if temp == "ONE":
        binary += "1"
        temp = ""
    elif temp == "ZERO":
        binary += "0"
        temp = ""

print(binary)
print(binascii.unhexlify('%x' % int(binary, 2)).decode())
