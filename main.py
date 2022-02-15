## Demo RSA encryption in Python code 
## Author : Paul Miailhe
## Date : 02/14/2022

## File containing all the essentials for the operation of RSA
from random import randint
from turtle import clear
import function

## Generate key :
    ## Parameter of the private key and the public key :
p = 0 # Distinct prime numbers
q = 0 # Distinct prime numbers
e = 0 # Public key 
d = 0 # Private key | inverse e modulo ϕ(pq) 
n = 0 # n=p.q R.S.A. Data Security recommends 
      # numbers n pq = ⋅ of 1024 bits (309 digits in base 10) 
      # base 10) or 2048 bits (617 digits in base 10).
   
    ## Data Test : 
text = "Test RSA demo 1 | 02/14/2022"

print("\nDemo encryption in Python code\n")

p = randint(1,100000000000)
p = function.higherPrime(p)
print(" - Distinct prime numbers p : ", p)

q = function.higherPrime(p*2)
print(" - Distinct prime numbers q : ", q)
print("\n")

p, q, d, e, n = function.keyRSA(p,q)

print (" - The private key (d;p;q) : ", d, ";", p, ";", q)
print (" - The public key (e;n) : ", e, ";", n)
print("\n")

print (" - sentence to encrypt : ", text)

L, M = function.TextToRSA(text,e,n)

print (" - Unencrypted message : ", L)
print (" - Crypted message : ", M)
print("\n")

D, TextD  = function.RSATtoText(M,d,n)

print (" - Deciphered message : ", D)
print(" - Sentence to decipher : ", TextD)









