def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

print lcmm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) 
