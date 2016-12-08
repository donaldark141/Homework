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
    
    
def foldlnew(f, x0, lst):
    return foldr(lambda x,y: lambda u: y(f(u,x)), lambda x: x, lst)(x0)
    
def foldrnew(f, x0, lst):
    return foldl(lambda y,x: lambda u: y(f(x,u)), lambda x: x, lst)(x0)




# Задание 2
import collections

def check_inv(a, b):
    b_counter = collections.Counter(b)
    i = 0
    while(i <= len(a) - len(b)):
        a_plus_counter = collections.Counter(a[i:i + len(b)])
        if a_plus_counter==b_counter:
            return True            
        i+=1
    return False
a = 'abcrotm'
b = 'tro'
print(check_inv(a,b))  



    
       
        
        





