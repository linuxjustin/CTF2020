from pwn import *
import string
conn=remote("212.47.229.1","33002")

sd=conn.recv()
sd=sd.split("\n")
sd=sd[4]
sd=sd.split(" ")
sd=sd[2]
print sd
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
out =string.translate(sd, rot13)
print out
sen= conn.sendline(out)

qw=conn.recv()
qw=qw.split()
qw=qw[1]
print qw
done=string.translate(qw, rot13)
print done
fin=conn.sendline(done)
#er=conn.recv()
#print er
while True:
    qw=conn.recv()
    print qw
    qw=qw.split()
    #print qw
    qw=qw[1]
    #print qw
    done=string.translate(qw, rot13)
    print done
    fin=conn.sendline(done)
    #er=conn.recv()
    #print er
