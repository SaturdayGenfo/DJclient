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
        style = "<head><style> table { margin-top: 42px; color:rgb(67, 173, 165);} td {padding : 9px; } </style></head>"
        ranking = [style, '<table>']
        for i, l in enumerate(lines):
            user, sc = l.strip("\n").split(' ')
            ranking.append("<tr>" + "<td>"+str(i+1)+ ". </td>"+"<td> <b>"+ user + "</b>"+ "</td> <td>" + sc + "</td>"+  "</tr>")
        ranking.append("</table>")
        return ranking
        