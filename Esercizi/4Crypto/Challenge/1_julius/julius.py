import base64
# Julius,Q2Flc2FyCg==
# -------------------
#
# World of Cryptography is like that Unsolved Rubik's Cube, given to a child that has no idea about it. A new combination at every turn.
#
# Can you solve this one, with weird name?
#
# ciphertext: fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==

ciphertext = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
toB64 = base64.b64decode(ciphertext)

print(toB64)

for i in range(0, 256):
    result = ""
    for j in range(0, len(toB64)):
        result += chr((toB64[j] + i) % 256)
    print(result)
    # encryptCTF{3T_7U_BRU73?!}