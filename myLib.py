def ModPow(a,n,m):
    y = 1
    while n>0:
        if n & 1:
            y = (y*a) % m
        n >>= 1
        a = (a*a) % m
    return y

def Primes(N):
    primes = [i for i in range(1, N+1)]
    primes[0] = 0
 
    for i in range(0, N):
        if primes[i] != 0:
            for j in range(i+primes[i], N, primes[i]):
                primes[j] = 0
 
    return [x for x in primes if x != 0]

def gcd(a,b):
    if(b == 0):
        return a
    return gcd(b,a%b)

def IsPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if not (n % i):
            return False
    return True

import random
def MillerRabinTest(n, k):
    if n <= 1:
        return False
    if n == 2:
        return True
    if not(n % 2):
        return False
    s = 0
    d = n-1
    while d%2 == 0:
        d >>= 1
        s += 1
    for i in range(k):
        a = random.randrange(2, n)
        x = ModPow(a,d,n)
        if x == 1 or x == n-1:
            continue
        for j in range(s - 1):
            x = (x*x) % n
            if x == 1:
                return False
            if x == n-1:
                break
        if x != n-1:
            return False
    return True

def sqrt(n):
    if n == 0:
        return 0
    x1 = n
    x2 = (x1 + n // x1) // 2
    while(x2 < x1):
        x1 = x2
        x2 = (x1 + n // x1) // 2
    return x1

def GetPeriod(a,m):
    if a==1:
        return 1
    f = [x for x in range(2,(m-1)//2 + 1) if (m-1) % x == 0]
    if(len(f)==0):
        return m-1
    for div in f:
        b = ModPow(a,div,m)
        if b == 1:
            return div        
    return m-1

def ExtendedAlgEuklid(a,b,m):
    xPrev = 1
    yPrev = 0
    r = b
    rPrev = a
    x = 0
    y = 1
    while r != 0:
        q = rPrev // r
        t = r
        r = rPrev % r
        rPrev = t
        t = x
        x = xPrev - (q * x) % m
        xPrev = t
        t = y
        y = yPrev - (q * y) % m
        yPrev = t
        if (x < 0):
            x += m
        if (y < 0):
            y += m
    return [rPrev, xPrev, yPrev]

def SearchInverse(a,m):
    d = ExtendedAlgEuklid(m,a,m)
    if(d[0] == 1):
        return d[2]
    return 0

primeNums = Primes(5000)
def GetPrime(countBits):
    random.seed()
    while True:
        a = random.getrandbits(countBits)
        a |= 1 << countBits - 1
        a |= 1 
        nextIter = False
        for primeNum in primeNums:
            if a // primeNum == 1:
                return a
            if a % primeNum == 0:               
                nextIter = True
                break  
        if nextIter:
            continue 
        if MillerRabinTest(a,countBits):
            return a    
