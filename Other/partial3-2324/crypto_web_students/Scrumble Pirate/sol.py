with open("challenge.txt", "r") as file:
    cipher = ''.join(file.readlines())

#Frequency Analysis function - useful when we have no information about the cipher text
def frequencyAnalysis(cipherText):
    freq = {}
    for i in cipherText:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

#Driver code
freq = frequencyAnalysis(cipher)
for i in sorted(freq.keys()):
    print(i, freq[i])

cipher = cipher.replace('L', 'e')
cipher = cipher.replace('A', 'h')
cipher = cipher.replace('S', 't')
cipher = cipher.replace('E', 'o')
cipher = cipher.replace('H', 'a')
cipher = cipher.replace('D', 's')
cipher = cipher.replace('U', 'l')
cipher = cipher.replace('P', 'r')
cipher = cipher.replace('R', 'u')
cipher = cipher.replace('O', 'n')
cipher = cipher.replace('Y', 'd')
cipher = cipher.replace('C', 'w')
cipher = cipher.replace('M', 'p')
cipher = cipher.replace('X', 'i')
cipher = cipher.replace('T', 'z')
cipher = cipher.replace('Q', 'k')
cipher = cipher.replace('Z', 'c')
cipher = cipher.replace('N', 'y')
cipher = cipher.replace('V', 'f')
cipher = cipher.replace('F', 'b')
cipher = cipher.replace('K', 'm')
cipher = cipher.replace('W', 'g')

print(cipher)