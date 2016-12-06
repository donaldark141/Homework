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
    
    
def foldl2(f, x0, lst):
    return foldr(lambda x,y: lambda u: y(f(u,x)), lambda x: x, lst)(x0)
    
def foldr2(f, x0, lst):
    return foldl(lambda y,x: lambda u: y(f(x,u)), lambda x: x, lst)(x0)




# Задание 2
from collections import Counter

def check_inv(a, b):
    cnt_b = Counter(b)
    i = 0
    while(i <= len(a) - len(b)):
        cnt_sub_a = Counter(a[i:i + len(b)])
        if cnt_b==cnt_sub_a:
            return True            
        i+=1
    return False     



    
       
        
        





