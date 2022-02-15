## Demo RSA encryption in Python code 
## Author : Paul Miailhe
## Date : 02/14/2022

import sys
import random
import string
import binascii
from binascii import unhexlify
from random import *
import math as mt

## Quick Exponentiation:
    ## Fast exponentiation algorithm for the calculation of x^e mod n
def exp(M,e,n):
    temp=1
    while e>0:
        if e%2==1:
            temp=(temp*M)%n
        M=(M*M)%n
        # With the arithmetic operator // the quotient is an integer
        e=e//2 
    return temp

##PGCD algorithm:
    ## Calculation PGCD of two positive integers
def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)

##Algorithm bezout:
    ## Calculation of the Bezout coefficients
def bezout(a,b):

    # U and V is Bezout coefficients
    U=[1,0]
    V=[0,1]
    i=1

    while b!=0:
        q=a//b
        r=a%b
        a=b
        b=r

        # Calculation of the new coefficients
        newU=U[i-1]-q*U[i]
        newV=V[i-1]-q*V[i]

        # Add to the vector the new coefficients
        U.append(newU)
        V.append(newV)
        i=i+1
    return U[i-1] , V[i-1]

##Reverse Modulo:
    ## Calculation of the inverse of a mod n
def invMod(a,n):
    d=pgcd(a,n)
    if d!=1:
        return False
    else:
        u,v=bezout(a,n)
    return u%n

    ## Used to confirm the detection of a prime number
def PrimalityTest(a):   
    if a == 2 :
        return True
    elif a % 2 == 0 :
        return False
    else :
        # i is odd, 
        # int is used to cast and edit floats
        # range (min, max, inc)
        # Use sqrt to minimize the number of operations 
        for i in range(3,int(mt.sqrt(a)),2) :
            if a % i == 0 : 
                return False
        return True

## higher prime:
        ## etermine the higher prime numbe :
def higherPrime(n):
    if n%2==0:
        n=n+1
    while PrimalityTest(n)==False:
            n=n+2
    return  n

##RSA key generation:
        ## Generates the private key (p;q;d) and the public key (e,n) 
def keyRSA(p,q):      
    n=p*q
    phi=(p-1)*(q-1)
    
    # According to the RSA standard min 3
    e=2 
    while pgcd(e,phi)!=1 :
        e=e+1
    d=invMod(e,phi)
    return p,q,d,e,n

##Rand RSA key generation:
        ## Generates the private key (p;q;d) and the public key (e,n) 
def keyRSARand(c):  
    p=higherPrime(c)    
    q=higherPrime(2*p)
    n=p*q
    phi=(p-1)*(q-1)
    
    # According to the RSA standard min 3
    e=3 
    while pgcd(e,phi)!=1 :
        e=e+1
    d=invMod(e,phi)
    return p,q,d,e,n

##Convert ASCII string to number
        ##Conversion of a character 
        ##string into integer using the ASCII code
def blockTXTtoNB(text):
    L =[]
    for ch in text:
        L.append(ord(ch))

    return L  

##Convert number to ASCII string 
        ## Convert a list of integers into a 
        ## string using the ASCII code
def blockNBtoTXT(L):    
    text =""
    for nb in L:
        ch=chr(nb)
        text=text+ch
    return text      

##Ciphers the text
        ## Conversion of a character string into 
        ## numerical equivalent ASCII by blocks of 
        ## length b>=1 and then RSA encryption of exponent k modulo n
def TextToRSA(text,e,n):
    L=blockTXTtoNB(text)    
    M=[]
    for nb in L:
        nb=exp(nb,e,n)
        M.append(nb)
    return L, M    

##Decipher the text
    ## RSA decryption of exponent k modulo n
    ## and then conversion of the blocks of length b>=1
    ## into a character string using the ASCII code

def RSATtoText(C,d,n):
    M=[]
    for elem in C:
        nbr=exp(elem,d,n)
        M.append(nbr)
    #text=blockNBtoTXT(M) 
    text = blockNBtoTXT(M)  
    return M ,text
    

