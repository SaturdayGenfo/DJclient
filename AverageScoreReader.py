# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:29:37 2017

@author: leello
"""

class ScoreReader():
    
    def __init__(self, filename):
        self.filename = filename
        
    
    def read(self, n):
        f = open(self.filename, 'r')
        lines = f.readlines()
        f.close()
        T = []
        S = []
        for line in lines[-n:]:
            l = line.split(' ')
            t, s = float(l[0][:-2]), int(l[1][:-2])
            T.append(t)
            S.append(s)
        return T,S
    
    
    
    
    