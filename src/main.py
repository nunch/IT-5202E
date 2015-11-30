'''
Created on 26 nov. 2015

@author: yo
'''
from RSA import RSA
import time

if __name__ == '__main__':
    rsa = RSA()
    #truc=rsa.primeFactorsDecomposition(1234567890123456789)
    a={1:2,3:9}
    a=5
    truc=0
    start_time = time.time()
    #truc=rsa.pollard(26915353)
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print(truc)
    
    start_time = time.time()
    truc=rsa.quadraticSieve(10585477741304331)
    elapsed_time = time.time() - start_time
    print(truc)
    print(elapsed_time)