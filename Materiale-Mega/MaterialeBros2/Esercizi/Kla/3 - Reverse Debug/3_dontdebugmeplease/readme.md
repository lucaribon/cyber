# Non è una CTF

# Write-up
1. Proviamo ad eseguire un run da gdb del binario: ci viene ritornato "there is already a debugger"
2. Se analizziamo da ghidra, c'è un if che controlla il ptrace (quindi l'intervento di GDB)
3. Soluzione: patchare l'if di controllo del ptrace