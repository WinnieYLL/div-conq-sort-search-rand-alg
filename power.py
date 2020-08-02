import numpy as np

def slowPower(a, b):
    ans = 1;
    for i in range(b):
        
        ans = ans * a
        
        # print("i = ", i)
        # print("ans =", ans)
        
    return ans

def fastPower(a,b):
    if b == 1:
        return a
    
    asquared = a*a
    number = fastPower(asquared,np.floor(b/2))
    
    if b % 2 == 1:
        return number*a
    else:
        return number