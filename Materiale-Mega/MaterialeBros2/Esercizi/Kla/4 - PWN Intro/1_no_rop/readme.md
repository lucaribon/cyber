# Flag
Flag={hello_world_pwn}

# Write-up
1. Analizziamo il file ``no_rop.c``
2. Possiamo vedere la dichiarazione delle variabili: viene dichiarata prima `pass`, variabile intera usata come flag booleana (vedi `if`) e una stringa `buff` di 8 caratteri (array di char)
3. Vengono messe in stack in ordine (quindi prima `pass` e poi `buff`): possiamo pensare allo stack pointer posizionato su `buff` e scrivere da quell'indirizzo a salire (ricordiamo che l'ultimo elemento dello stack ha indirizzo più basso in quanto lo stack evolve verso il basso, ma la scrittura avviene secondo l'ordine di memoria, quindi verso l'alto). Quando andiamo quindi a inserire l'input per `buff`, andiamo a inserire 9 caratteri invece di 8, facendo attenzione che l'ultimo carattere sia diverso da 0
4. Salvare la Flag