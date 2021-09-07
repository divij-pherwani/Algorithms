import sys
import numpy as np
import bisect
 
def waiting_times(n,k,prices,gains):
    ret=[]                                   
    p =  np.array(prices) 
    sp = sorted(p)
    flag = ~(np.all(p[:-1] <= p[1:]))
    index = np.argsort(p, kind = 'mergesort')
    
    for j in gains:                                                             
        s = prices[0] + j                                                       
        try:
            #temp = find_ge(sp,s,c,n) 
            t1 = find_lge(sp,s,0,n) 
            r1 = index[t1]
            t2 = find_rge(sp,s,0,n) 
            r2 = index[t2]
            res = min(r1,r2)
            if flag:
                for i in range(res+2//2):
                    if p[i] >= s:
                        res = i
                        break
                    elif (p[res-i] >= s):
                        res = res - i
        except ValueError:
            res = n        
        ret.append(res)
    return ret
    
def find_lge(a, x, lo, hi):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x, lo, hi)
    if i != len(a):
        return i
    raise ValueError
    
def find_rge(a, x, lo, hi):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_right(a, x, lo, hi)
    if i != len(a):
        return i
    raise ValueError


astr = sys.stdin.readline().split()
n=int(astr[0])
k=int(astr[1])
astr = sys.stdin.readline().split()
a=[int(s) for s in astr[0:n]]
astr = sys.stdin.readline().split()
b=[int(s) for s in astr[0:k]]
c = waiting_times(n,k,a,b)
for waitingtime in c:
    print(str(waitingtime))