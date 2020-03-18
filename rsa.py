from factordb.factordb import FactorDB

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



string=raw_input("Enter the N: ")
e=raw_input("Enter the E: ")
c=raw_input("Enter the Ciper:")
byted_str = int(string)
f = FactorDB(byted_str)
f.get_factor_list()
f.connect()
out = f.get_factor_list()

print out

p = out[0]
 
q = out[1]

n = byted_str
e = int(e)
c = int(c)

fi = (p-1)*(q-1)
d = modinv(e, fi)
print ("%x" % pow(c, d, n)).decode("hex")
