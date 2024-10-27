from Crypto.Util.number import bytes_to_long, getPrime
from secrets import flag1, flag2, flag3
from os import urandom

flag1 = bytes_to_long(flag1)
flag2 = bytes_to_long(flag2)
flag3 = bytes_to_long(flag3)

p, q, r, s = [getPrime(512) for i in range(4)]

e = 0x10001

n1 = p * q
n2 = q * r
n3 = r * s

c1 = pow(flag1, e, n1)
c2 = pow(flag2, e, n2)
c3 = pow(flag3, e, n3)

booo = bytes_to_long(urandom(69))   # H4PPY H4LL0W33N GUYZZZZ

print(f'n1: {n1}')
print(f'c1: {c1}')
print(f'c2: {c2}')
print(f'c3: {c3}')
print(f'(n1 * booo) + n2: {n1 * booo + n2}')  
print(f'(r * booo) + s: {r * booo + s}')     
