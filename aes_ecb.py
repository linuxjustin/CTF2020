import requests
from string import printable


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "SOMETHING",
    "Cookie": "SOMETHING",
    "Connection": "close",
    "Content-Type": "application/json"
}

url = "http://206.189.141.41:8000/genCookie"

def get_token(token):
    block_size=64
    new=[]
    for i in range(0,len(token),block_size):
        new.append(token[i:i+block_size])
    return new


flag=''
for i in reversed(range(1,32)):
    sev1="a"*i
    #print sev1
    dd1='{"username":' + '"'+sev1+ '"'  + '}'
    conn=requests.post(url,headers=headers,data=dd1)
    sd= conn.content
    #print sd
    sd=sd.split('"')
    sd=sd[3]
    sd=str(sd)
    #print sd
    out2=get_token(sd)
    print out2
    alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];,./!@#$%^&*()_+{}|:<>?"
    for x in alph:
    	sev=sev1+flag+x
    	#print sev
        dd1='{"username":' + '"'+sev+ '"'  + '}'
        conn=requests.post(url,headers=headers,data=dd1)
	sd= conn.content
	#print sd
	sd=sd.split('"')
	sd=sd[3]
	sd=str(sd)
	#print sd
	out=get_token(sd)
        print out
        if out2[0]==out[0]:
            print "WOOW GOT HIT" , x
            flag+=x
            break
    print flag
    if '}' in flag:
        break
