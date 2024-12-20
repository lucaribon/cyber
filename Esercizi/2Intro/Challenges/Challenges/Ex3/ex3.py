# Define a randomic password generator.
# The password should contain 10 characters.
# Type of characters: alphanumeric
import random
import string

res = ""
i = 0
for i in range(10):
    res += random.SystemRandom().choice(string.ascii_letters + string.digits)
    i += 1

print(res)


