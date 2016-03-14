#!/usr/bin/env python

Empty = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
# Empty Single column
E_S = [[0],
       [0],
       [0],
       [0],
       [0],
       [0],
       [0],
       [0]]

Exclamation = [[1],
               [1],
               [1],
               [1],
               [1],
               [1],
               [0],
               [1]]

A = [[0,0,0,1,1,0,0,0],
     [0,0,1,0,0,1,0,0], 
     [0,1,0,0,0,0,1,0], 
     [1,0,0,0,0,0,0,1], 
     [1,1,1,1,1,1,1,1], 
     [1,0,0,0,0,0,0,1], 
     [1,0,0,0,0,0,0,1], 
     [1,0,0,0,0,0,0,1]]

B = [[1,1,1,1,1,1,1,0],
     [1,0,0,0,0,0,0,1], 
     [1,0,0,0,0,0,0,1], 
     [1,1,1,1,1,1,1,0], 
     [1,1,1,1,1,1,1,0], 
     [1,0,0,0,0,0,0,1], 
     [1,0,0,0,0,0,0,1], 
     [1,1,1,1,1,1,1,0]]

C = [[0,0,1,1,1,1,1,0],
     [0,1,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [0,1,0,0,0,0,0,1],
     [0,0,1,1,1,1,1,0]]


D = [[1,1,1,1,1,1,0,0],
     [1,0,0,0,0,0,1,0],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,1,0],
     [1,1,1,1,1,1,0,0]]


E = [[1,1,1,1,1,1,1,1],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1]]

H = [[1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1]]

I = [[1,1,1,1,1,1,1,1],
     [0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0,0],
     [1,1,1,1,1,1,1,1]]

K = [[1,0,0,0,0,1,1,0],
     [1,0,0,0,1,0,0,0],
     [1,0,0,1,0,0,0,0],
     [1,0,1,0,0,0,0,0],
     [1,1,1,0,0,0,0,0],
     [1,0,0,1,0,0,0,0],
     [1,0,0,0,1,0,0,0],
     [1,0,0,0,0,1,1,0]]

L = [[1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1]]

O = [[0,0,1,1,1,1,0,0],
     [0,1,0,0,0,0,1,0],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,1],
     [0,1,0,0,0,0,1,0],
     [0,0,1,1,1,1,0,0]]


P = [[1,1,1,1,1,1,0,0],
     [1,0,0,0,0,0,1,0],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,1,0],
     [1,1,1,1,1,1,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0]]

R = [[1,1,1,1,1,1,0,0],
     [1,0,0,0,0,0,1,0],
     [1,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,1,0],
     [1,1,1,1,1,1,0,0],
     [1,0,0,1,0,0,0,0],
     [1,0,0,0,1,0,0,0],
     [1,0,0,0,0,1,1,1]]

W = [[1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [1,0,0,1,0,0,0,1],
     [0,1,1,0,1,1,1,0]]

