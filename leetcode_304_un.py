#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:14:45 2017

@author: jie
"""
import numpy

def NumMatrix(mat):
    if len(mat)==0 or len(mat[0])==0: return 0
    m=len(mat)
    n=len(mat[0])

    tree= numpy.zeros(shape=(m+1,n+1))
    nums= numpy.zeros(shape=(m,n))
    
    for i in range(m):
        for j in range(n):
            updatebit(mat,m,n,tree,nums,i,j,mat[i][j])
    return tree


def updatebit(mat,m,n,tree,nums,row , col ,val):
    delta=val-nums[row][col]
    nums[row][col]=val
        
    for i in range(row+1,m+1):
        for j in range(col+1,n+1):
            tree[i][j]+=delta
            j += j & (-j)          
        i += i & (-i)


def SumRegion(tree,row1,col1,row2,col2):
    return getsum(tree,row2+1,col2+1)
    
def getsum(tree,row,col):
    s = 0  
    i = row # index in BITree[] is 1 more than the index in arr[]

    while i > 0:
        j=col
        while j>0:
            s+=tree[i][j]
            j-=j & (-j)
        i -= i & (-i)
    return s

freq = [[3,0,1],[5,6,3],[1,2,0],[4,1,0]]
BITTree = NumMatrix(freq)
print(freq)     
print(BITTree)

print(getsum(BITTree,2,2))








            
    


        
        
        
        
        
        
        
        
        
        

        
