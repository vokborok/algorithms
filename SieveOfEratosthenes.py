# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(N):

    # Create a boolean array "L[0..N]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    L = [True]*N
    L[0]=L[1]=False
    for i in range(2,N):
      if L[i]:
        for m in range(2*i,N,i):
          L[m]=False
    for i in range(N):
       print(i,"-","prime" if L[i] is True else "not pirme")

# driver program
if __name__=='__main__':
    N = 1000
    print "Following are the prime numbers smaller",
    #Use print("Following are the prime numbers smaller") for Python 3
    print "than or equal to", N
    #Use print("than or equal to", n) for Python 3
    SieveOfEratosthenes(N)