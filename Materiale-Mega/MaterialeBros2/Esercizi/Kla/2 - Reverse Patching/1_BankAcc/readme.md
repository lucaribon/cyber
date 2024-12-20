# Flag
Flag{P00r_45_DuCk}

# Write-up
## Soluzione con Ghidra
1. In un primo momento, analizzando il decompilato, possiamo vedere che il PIN è un numero generato casualmente, mentre la FLAG è criptata mediante una funzione decrypt
2. Possiamo però vedere un IF che controlla l'uguaglianza tra il PIN inserito e quello generato randomicamente
3. Posso sostituire l'istruzione ASM JNZ a JZ, o mettere a NOP

## Soluzione con IDA
//TODO 