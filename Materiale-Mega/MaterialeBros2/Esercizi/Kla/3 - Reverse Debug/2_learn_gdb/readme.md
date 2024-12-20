# Flag
picoCTF{gDb_iS_sUp3r_u53fuL_f3f39814}

# Write-up
1. Aprire gdb su run
2. Impostare come breakpoint il punto prima del ret
3. Eseguire "run"
4. Ora il programma ci informa che il dato è immagazzinato in una variabile globale "flag_buf"
5. con "info address flag_buf", sappiamo dove flag_buf si trova
6. Se si prova a stampare con x/s flag_buf, questo non stamperà la flag
7. flag_buf contiene un puntatore, quindi l'unica è castare il x/s flag_buf con x/s (char*)flag_buf