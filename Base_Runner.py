i#Base Runner
from pwn import *
import base64
conn=remote("chals20.cybercastors.com",14430)
#conn.sendline("\n")
#print conn.recvuntil("Hit <enter> when ready.")
#print conn.recv()
#conn.sendline("\n")
sd= conn.recvlines(13)
conn.sendline("0")
out=conn.recvline()
out=out.replace("\n","")
print out

a_binary_string=out

ascii_string = "".join([chr(int(binary, 2)) for binary in a_binary_string.split(" ")])
#print ascii_string

def octal_to_str(octal_str):
    
    #It takes an octal string and return a string
     #   :octal_str: octal str like "110 145 154"
    
    str_converted = ""
    for octal_char in octal_str.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted


sd=(octal_to_str(ascii_string))

sd=sd.replace(" ","")
print sd
out=sd.decode("hex")
final=base64.b64decode(out)
print final
conn.sendline(final)

e=1
for x in range(50):

        conn.recvline()
        #print conn.recvline()
        nic= conn.recvline()
        nic=nic.replace("\n","")
        #print nic
        a_binary_string=nic

        ascii_string = "".join([chr(int(binary, 2)) for binary in a_binary_string.split(" ")])
        #print ascii_string

        def octal_to_str(octal_str):
            
            #It takes an octal string and return a string
             #   :octal_str: octal str like "110 145 154"
            
            str_converted = ""
            for octal_char in octal_str.split(" "):
                str_converted += chr(int(octal_char, 8))
            return str_converted


        sd=(octal_to_str(ascii_string))

        sd=sd.replace(" ","")
        #print sd
        out=sd.decode("hex")
        final=base64.b64decode(out)
        print final
        conn.sendline(final)
        #print conn.recvline()
        e=1+e
        print e
        if e==50:
                print conn.recv()
