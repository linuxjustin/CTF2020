#Password 3
import hashlib


f = open('pass', 'rb')
for z in f:
    d = z.replace("\n","")
    d="castorsCTF{"+d+"}"
    #print d
    s = hashlib.sha256(d).hexdigest()
    print d
    if "7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12" == s:
        print "flag is" , d
