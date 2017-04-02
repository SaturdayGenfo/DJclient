# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:09:13 2017

@author: leello
"""

class RankingReader():
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        f = open(self.filename, 'r')
        lines = f.readlines()
        f.close()
        ranking = []
        for i, l in enumerate(lines):
            ranking.append(str(i+1)+". "+ l.strip("\n"))
        return ranking
        