from pwn import *
conn=remote("212.47.229.1", "33003")

sd=conn.recv()
sd=sd.split("\n")
sd= sd[3]
sd=sd.split()
print sd
print sd[1],sd[2],sd[3]
err=sd[2]
print err
sym=err

if sym=="XOR":
    caluc = int(sd[1]) ^ int(sd[3])

    print caluc
elif sym=="OR":
    caluc= int(sd[1]) | int(sd[3])
    print caluc
elif sym=="AND":
    caluc= int(sd[1]) & int(sd[3])
    print caluc
print caluc
caluc=str(caluc)
se =conn.sendline(caluc)

while True:
    sd=conn.recv()
    #print sd
    sd=sd.split()
    print sd
    sym=sd[2]
    #nu=sd[1]
    #se=sd[2]
    #num1=sd[3]
    #print nu,se,num1

    if sym=="XOR":
        caluc = int(sd[1]) ^ int(sd[3])

        print caluc
    elif sym=="OR":
        caluc= int(sd[1]) | int(sd[3])
        print caluc
    elif sym=="AND":
        caluc= int(sd[1]) & int(sd[3])
        print caluc
    print caluc
    caluc=str(caluc)
    se =conn.sendline(caluc)
    #sd =conn.recv()
    #print sd
