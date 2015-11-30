'''
Created on 26 nov. 2015

@author: yo
'''
from random import randint
import math
import sys
import operator

class FoundException(Exception):
    pass

class RSA:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def squareAndMultiply(self,m,e,n):
        bin_e=bin(e)[2:]
        max_bin=len(bin_e)
        c=m
        for i in range(1,max_bin):
            c=c*c
            if(bin_e[i]=='1'):
                c=c*m
            c=c%n
        return c
            
    def multiplyAndReduce(self,a,b,n):
        m=a*b
        r=m%n
        return r
    
    def modularMultiplication(self,a,b,k,n):
        r=0
        for i in range(k-1,-1,-1):
            r=r*2
            #if()
    
    def isPrime(self,n):
        if n % 2 == 0 and n > 2: 
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

    def getPrimes(self,n):
        res=[]
        for i in range(1,n+1):
            if self.isPrime(i):
                res.append(i)
        return res
    
    def getAlphas(self,n):
        primes = self.getPrimes(n)[1:]
        res=[]
        for number in primes:
            alpha=1
            while pow(number, alpha)<=n:
                alpha+=1
            res.append([number,alpha-1])
        return res
    
    def pgcd(self,a,b):
        """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
        while b!=0:
            a,b=b,a%b
        return int(a)
    
    def isCoprime(self,a,b):
        return self.pgcd(a, b)==1
    
    def chooseA(self,n):
        for i in range(2,n):
            if self.isCoprime(i, n):
                return i
            
    
    def pollard(self,n):
        a=self.chooseA(n)
        b=2
        while 1==1:
            alphas=self.getAlphas(b)
            m=1
            for couple in alphas:
                m*=pow(couple[0],couple[1])
            am = pow(a,m)
            pgcd = self.pgcd(am-1,n)
            if ((am-1)%n!=0) and pgcd!=1:
                return [pgcd,n*1.0/pgcd]
            else:
                b+=1
            if b==n:
                return [False]
            
    def pollard2(self,n,a,b):
        alphas=self.getAlphas(b)
        print(alphas)
        m=1
        for couple in alphas:
            m*=pow(couple[0],couple[1])
        am = pow(a,m)
        pgcd = self.pgcd(am-1,n)
        if ((am-1)%n!=0) and pgcd!=1:
            return [pgcd,n*1.0/pgcd]
        else:
            return [False,m,pgcd]   
        
    def primeFactorsDecomposition(self,n):
        tuples={}
        if(n<0): 
            n=-n
            tuples[-1]=1
        prime=[2]
        if (n < 2):
            return None
        else:
            max = long(math.sqrt(n)) + 1
            for j in prime:
                if (j > n):
                    break
                if (n % j):
                    continue
                 
                i=0
                while not (n % j):
                    i+=1
                    n/=j
     
                if (i > 0):
                    tuples[j]=i
     
            if (prime[-1] % 2):
                #print("prime : "+str(prime[-1]))
                min=prime[-1]+2
            else:
                min=3
     
            for j in xrange(min, max, 2):
                if (j > n):
                    break
                if (n % j):
                    continue
                
                i=0
                while not (n % j):
                    i+=1
                    n/=j
     
                if (i == 0):
                    print ("Error for j=" + str(j))
                    sys.exit(1)
     
                tuples[j]=i
        if (n > 1):
            tuples[n]=1
        return tuples
    


    def isSquare(self,decomp):
        for key in decomp:
            if decomp[key]%2!=0:
                return False
        return True
    
    def multiplicateCouples(self,a,b):
        res={}
        for key in a:
            if key not in b:
                res[key]=a[key]
            else:
                res[key]=a[key]+b[key]
        for key in b:
            if key not in a:
                res[key]=b[key]
        return res
            
    def calculateCouple(self,a):
        res=1
        for key in a:
            res*=key*a[key]
        return res
    
    def sqrtCouple(self,a):
        res={}
        for key in a:
            res[key] = a[key]/2
        return res
    
    def quadraticSieve(self,n):
        T=int(math.floor(math.sqrt(n)))
        x=[]
        y=[]
        xx=0
        yy=0
        yDecomp=[]
        m=math.floor(math.sqrt(n))
        found=False
        square=0
        simple=0
        keep=True
        while found==False:
            T+=1
            print(T)
            x=[]
            y=[]
            yDecomp=[]
            for j in range(-T,T+1):
                t=j+T
                x.append(t+m)
                #print("t="+str(t)+" m="+str(m) + " t+m="+str(t+m))
                
                Py = (t+m)*(t+m)-n
                y.append(Py)
                
                PyDecomp = self.primeFactorsDecomposition(Py)
                yDecomp.append(PyDecomp)
                if (self.isSquare(PyDecomp)):
                    found=True
                    square=yDecomp
                    xx=x[t]
                    simple=self.sqrtCouple(PyDecomp)
                    yy=self.calculateCouple(simple)
                    print("youpi")
                    break
            if found==False:
                try:
                    for i in range (0,2*T+1):
                        for j in range(0,2*T+1):
                            if i!=j:
                                ij=self.multiplicateCouples(yDecomp[i],yDecomp[j])
                                if self.isSquare(ij):
                                    square=ij
                                    raise FoundException
                except FoundException:
                    print("youpi2")
                    print(str(i)+":"+str(j)+" "+str(T))
                    print(yDecomp[i])
                    print(yDecomp[j])
                    print(square)
                    found=True
                    xx=x[i]*x[j]
                    simple=self.sqrtCouple(square)
                    yy=self.calculateCouple(simple)
                    print(str(xx) +" : "+str(yy))
        
        
        xx=xx%n
        yy=yy%n
        pgcd = self.pgcd(xx-yy, n)
        return [pgcd,n*1.0/pgcd,xx,yy,xx-yy,n*1.0/(xx-yy)]
          
            
            
            
            
            
            
            
            
            
            
            
            
            