# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:34:29 2022

@author: 郭耸
"""


x={7,8,9}
for i in x:
    a=i
    S=set()
    S.add(i)
    U=x-S
    for j in U:
        b=j
        e=S.copy()
        e.add(j)
        U=x-e
        c=list(U)[0]
        if c*100+b*10+b+b*10+a==a*100+b*10+c:
            print({'a':a,'b':b,'c':c})