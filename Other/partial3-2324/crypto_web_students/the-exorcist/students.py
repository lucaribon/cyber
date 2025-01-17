#!/usr/bin/env python3

import string
import itertools

ALPHABET=list(string.ascii_lowercase)+list(string.ascii_uppercase) 

def XORop(message, KEY):
    rep=len(message)//len(KEY) + 1
    key=(KEY*rep)[:len(message)] # adjust the key len
    xored=''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

with open('encrypted', 'r') as f:
    encrypted_flag=f.read()

perms=list(itertools.permutations(ALPHABET, 2))

for p in perms:
    KEY=p[0]+p[1]
    decrypted=XORop(encrypted_flag, KEY)
    if 'spritz' in decrypted:
        print(decrypted)