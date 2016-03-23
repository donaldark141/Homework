# -*- coding: utf-8 -*-
# Задание 1
def foldl(f, x0, lst):
    if not lst:
        return x0
    return foldl(f, f(x0, lst[0]), lst[1:])

def foldr(f, x0, lst):
    if not lst:
        return x0
    return f(lst[0], foldr(f, x0, lst[1:]))
    
    
def foldr2(f, x0, lst):
    lst1=lst[::-1]
    return foldl(f, x0, lst1)
    
def foldl2(f, x0, lst):
    lst1=lst[::-1]
    return foldr(f, x0, lst1)





# Задание 2
def check_inv(a, b):
    sB = (b)
    dcb = {k:b.count(k) for k in sB}
    i = 0
    while i <= (len(a) - len(b)):
        sSb = (a[i:i + len(b)])
        dSb = {k:b.count(k) for k in sSb}
        if sB == sSb and all(dcb[k]==dSb[k] for k in sB) : 
            return True
        i+=1
    return False         



    
       
        
        





