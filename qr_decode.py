from pwn import *
from PIL import Image
from subprocess import check_output
import re

def decode_qr(qr):
    img = Image.new('1', (len(qr), len(qr[0])))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (int(qr[j][i]) + 1) % 2
    img.save('qr_code_temp.png')
    decoded = check_output(["zxing", "qr_code_temp.png"])
    decoded = re.findall(r"'(.*?)'", decoded, re.DOTALL)[1]
    return(decoded)

r = remote('qr-generator.ctf.defenit.kr', 9000)

r.recvuntil('?')
r.sendline('warlock')

for _ in range(100):
    r.recvuntil('< QR >\n')
    qr_code = r.recvuntil('S')[:-3]
    r.sendline(decode_qr([v.split(' ')[:-1] for v in qr_code.split('\n')]))

r.interactive()
