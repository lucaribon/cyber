# Flag
Flage{reverse_hello_world}

# Write-up

## Soluzione con Ghidra
1. Trovo il codice del decompilato
2. Analizzo
3. Individuo un if_case in cui vengono comparati gli elementi dello stack in cui è stato inserito l'input da tastiera (ex. local14 a local10, dove possiamo pensare il numero del local come indice nello stack)
4. Dobbiamo inserire da tastiera Fl4g
5. Viene così invocata la funzione print_flag
(Se avessi voluto, potevamo prendere la print_flag direttamente dalla funzione)

## Soluzione con IDA
Anche qui, la soluzione è molto simile, ma non abbiamo il codice del decompilato; ci accontentiamo del graph view.
1. Analizzo la struttura
2. Vedo anche qui la presenza di un if_case, con condizioni collegate da &. Anche qui possiamo vedere che viene comparato Fl4g dall'input da rbp+varC in poi
3. Successivamente, se l'if va a buon fine, procede anche qui ad eseguire la funzione printflag, dove possiamo trovare la flag in chiaro