## Istruzioni assembly utili
- jmp -> Salta all'etichetta/locazione specificata 
- je -> Jump if Equal
- jz -> Jump if Zero
- jne -> Jump if not Equal
- jnz -> Jump if not Zero
- js -> Jump if negatuve
- jns -> Jump in notnegative
- jg -> Jump if greater 
- jge -> Jump if greater or equal 
- jl -> Jump if less
- jle -> Jump if less or equal 
- ja -> Jump if above 
- jae -> Jump if above or equal 
- jb -> Jump if below 
- jbe -> Jump if below or equal 
- jnb -> Jump if Condition Is Met

* call -> Push return address and jump to label 221
* leave -> Set %rsp to %rbp, then pop top of stack into %rbp
* ret -> Pop return address from stack and jump there

## Altre info
Vuknerabilità in C (buffer overflow):
- scanf
- read
- strcat
- fread
- fgets
- printf vulnerability
- sprintf
- strcpy
- getss
- memcpy
- memmove
- strcpy
- snprintf
- strncat
- fgets/fflush -> Da qualche parte in memoria si genera la flag

Entrypoint -> I punti in cui il programma prende un input di qualche tipo o file 

Controlli anti-debug:
- ptrace(); quando presente, controlla se c'è un debugger. 
Occorre fare in modo di farle ritornare 0 e non 1
- Controllo sulle variabili d'ambiente 
- Controllare la rilocazione dello heap (in BSS viene spostato e riassegnato)
- Controllare le sezioni .init e .fini o start (contengono i controlli anti-debug)