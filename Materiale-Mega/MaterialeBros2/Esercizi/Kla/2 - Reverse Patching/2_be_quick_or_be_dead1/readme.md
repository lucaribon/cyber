# Flag
picoCTF{why_bother_doing_unnecessary_computation_27f28e71}

# Write-up
## Soluzione con Ghidra
1. Provando l'esecuzione, il programma viene terminato in quanto afferma che la macchina è molto lenta
2. Analizzando il codice, troviamo all'interno di set_timer una funzione creata e nominata alarm_handler, che, al terminare di un lasso temporale, ci dice che la macchina è troppo lenta e fa exit(0)
3. La soluzione è quindi patchare l'exit, impostando un NOP
4. A quanto pare però succede un casino -> la scelta migliore sarebbe quindi evitare la chiamata a set_timer e navigare liberi
5. Proviamo dopo la patch, e questa soluzione funziona
