def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y


p = 7963
q = 16033
e = 7
ct = 27613890
n = 127670779

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute modular inverse of e
gcd, a, b = egcd(e, phi)
d = a


# Decrypt ciphertext
pt = pow(ct, d, n)
print( "pt: " + str(pt) )