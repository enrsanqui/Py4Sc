#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sieve_v1(n):
    """
        Use Sieve of Eratosthenes to compute list of primes <= n.
        Version 1
    """

    primes = range(2,n+1)
    for p in primes:
        if p*p>n:
            break
        product=2*p
        while product<=n:
            if product in primes:
                primes.remove(product)
            product+=p
    return len(primes),primes

def sieve_v2(n):
    """
       Sieve of Eratosthenes to compute list of primes <=n.
       Version 2
    """

    sieve = [True]*(n)
    for i in xrange(3,n+1,2):
        if i*i > n:
            break
        if sieve[i]:
            sieve[i*i: :2*i] = [False]*((n-i*i)//(2*i)+1)
        answer = [2] + [i for i in xrange(3,n+1,2) if sieve[i]]
        return len(answer), answer
