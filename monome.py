# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:16:39 2021

@author: Hansali haitam
"""

class Monome:
    
    def __init__(self, coef, deg, suivant=None):
        # donnée :
        self.coef = coef # de type float
        self.deg = deg # de type int
        # une reference vers le prochain monome (par défault None)
        self.suivant = suivant # de type Monome
        
    def getCoef(self):
        return self.coef
    
    def setCoef(self, val):
        self.coef = val
        return self
    
    def getDeg(self):
        return self.deg
   
    def setDeg(self, val):
        self.deg = val
        return self
    
    def getSuivant(self):
        return self.suivant
    
    def setSuivant(self, m):
        self.suivant = m
        return self
    
    def __str__(self):
        return str(self.getCoef()) + 'X^' + str(self.getDeg())
    
    def __mul__(self, m):
        return Monome(self.getCoef() * m.getCoef(), self.getDeg()+m.getDeg())
    
    def __add__(self, m):
        assert self.getDeg() == m.getDeg()
        return Monome(self.getCoef() + m.getCoef(), self.getDeg())
    
    @staticmethod
    def oppose(a):
        return -a
    
    def __sub__(self, m):
        assert self.getDeg() == m.getDeg()
        return Monome(self.getCoef() + Monome.oppose(m.getCoef()), self.getDeg())
            
    def __truediv__(self, m):
        assert self.getDeg() >= m.getDeg()
        return Monome(self.getCoef() / m.getCoef(), self.getDeg() - m.getDeg())
        
    @staticmethod
    def deriver(m):
        if m.getDeg() == 0:
            return 0
        else :           
            return m.getCoef() if m.getDeg() == 1 else Monome(m.getDeg() * m.getCoef(), m.getDeg()-1)
        
    @staticmethod   
    def primitive(m):
        return Monome(m.getCoef(), m.getDeg()+1) if m.getDeg() == 0 else Monome(m.getCoef() / (m.getDeg()+1),(m.getDeg()+1))