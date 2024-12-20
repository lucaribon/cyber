# Flag
TUCTF{d0n7_h4rdc0d3_p455w0rd5}

# Write-up

## Soluzione con Ghidra
1. Vedo che nello stack, dalla local1a fino alla local12 viene scritta una scritta (Ghidra non ce la scrive perfettamente, ma se si modifica il tipo si ottiene il risultato) -> La string contiene john galt.
2. Vedo che il primo input fa il strcmp con la stringa "john galt" -> possiamo dire che questo sia lo username
3. Come password, la password è salvata in un segmento in chiaro, ed è "this-password-is-a-secret-to-everyone!"
4. Riesco così ad accedere alla casella di posta e, visualizzando l'email, trovo la flag

## Soluzione con IDA
Con IDA si fa la stessa cosa, solo che è meno intuitivo capire il compare