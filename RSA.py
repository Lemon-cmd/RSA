from random import *

def genPrime():
    while True:
        p = randrange(10001, 100000, 2)
        if all(p % n!= 0 for n in range (3, int((p ** 0.5) + 1), 2)):
                return p

def totient(p , q):
    totient = (p - 1) * (q - 1)
    return totient

def gcd(e,t):
    x = e
    y = t
    
    while y != 0:
        (x, y) = (y, x % y)
        
    return x


def ext(a, b): 
        
        x , lastX = 0, 1
        y , lastY = 1, 0

        while (b != 0):
            q = a // b
            x, lastX = lastX - q * x, x
            y, lastY = lastY - q *y, y
            a, b = b, a % b
            
        return lastY

def trapdoor(p, q):
    n = p * q
    return n

def test(p ,q):
    while p == q:
        p = genPrime()
        q = genPrime()

    return p,q

def test2(p, q, e, t):
    while gcd(e, t) != 1:
        p = genPrime()
        q = genPrime()
        t = totient(p, q)

    return p,q,t

def createVar():
    e = 65537
    p = 0
    q = 0

    p, q = test(p ,q)

    t = totient(p , q)

    p, q, t = test2(p, q, e, t)
    
    n = trapdoor(p, q)
    d = ext(t, e)
    
    return e, t, n, d

def modularExp(m, e, n):
    x = 1
    convertE = bin(e)[2:]
    convertE = list(convertE)
    convertE.reverse()
    
    power = m % n
    for i in convertE:
        
        if i == '1':
            x = (x * power) % n
        power = (power * power) % n
        
    return x

def filee():
    file = input("Read file: ")
    infile = open(file, 'r')
    String = infile.read()
    return String


def output(text):
    file = input("Please enter the path to the file you wish to write to: ")
    openfile = open(file, 'w')
    print(text, file = openfile)
    openfile.close()
    
def Encrypt(e, n):
    print("Encryption")
    text = ""
    TextStr = filee()
    for i in TextStr:
        c = modularExp(ord(i),e,n)
        while len(str(c)) < 12:
            c = '0' + str(c)
        c = c + ' '
        text = text + c
    output(text)

def Decrypt(d, n):
    print("Decryption")
    text = ""
    TextStr = filee()
    TextList = TextStr.split()
    for i in TextList:
        m = modularExp(int(i), d, n)
        text = text + chr(m)
    output(text)

def main():
            
    e, t, n, d = createVar()
    Encrypt(e, n)
    print()
    Decrypt(d, n)
    

main()

    
