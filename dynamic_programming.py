'''
    Sometimes we may want to sacrifice some memory to make the code more efficient.
    we create a cache where we store repetitive tasks and avoid redundant calculations

    In this example, using the fib function is costly due to the repetitive calls, however in the second method, we can run even the fibonacci of several hundrends
    and get the results almost instantly
'''

def fib(n):
    ''' For small values'''
    if n<2:
        return n
    return fib(n-1) + fib(n-2)


cache = {}
calc = 0 # to see how many calls we make to the function. turns out to be n-1

def fibMem(n):
    '''fibonnacci using memoization'''
    global calc
    calc += 1
    
    if n in cache:
        return cache[n]
    else:
        if n<2:
            return n
        
        cache[n] = fibMem(n-1) + fibMem(n-2)
        return cache[n]

print(fibMem(998)) # a 209 character digit but within less than  0.5 seconds in my machine
#print(fib(998)) # this could mess up your stuff, its a bad idea.