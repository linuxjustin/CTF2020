import pwn
from pwn import *

conn=remote("crypto.chal.csaw.io",5001)
flag=[]
print conn.recv()
inp = 'a' * 32
conn.sendline(inp)
inpu=conn.recv()
inpu=inpu.split("\n")
out=inpu[0]
out=out.split("  ")
data=out[1]
print data[:32] 
print data[32:64]
conn.sendline("ECB")
flag.append("0")
for x in range(175):
	print conn.recv()
	inp = 'a' * 32
	conn.sendline(inp)
	inpu1=conn.recv()
	inpu1=inpu1.split("\n")
	out1=inpu1[0]
	out1=out1.split("  ")
	data1=out1[1]
	print data1[:32] 
	print data1[32:64]
        if data1[:32] == data1[32:64]:
            conn.sendline("ECB")
            flag.append("0")
        else:
            conn.sendline("CBC")
            flag.append("1")
        print flag
print flag
