# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:15:53 2021

@author: Hansali haitam
"""
class Polynome:
    def __init__(self, tete):
        self.tete = tete # est de type Monome
        
    def getTete(self):
        return self.tete
    
    def setTete(self, t):
        self.tete = t
        return self
    
    def est_vide(self):
        return self.getTete() == None
    
    
    def localiser(self, m):
        """
        localiser où situer convenablement un monome de même degré que m dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à situer dans le polynome appelant.
        Returns
        -------
        Monome.
        """
        
        r = self.getTete()
        p = r
        while r.getDeg() >= m.getDeg() and r != None :
            p = r
            r = r.getSuivant()
        return p
    
    def dernier(self):
        p = self.getTete()
        while p.getSuivant() != None:
            p = p.getSuivant()
        return p
    
    def ajouter(self, m):
        """
        inserer un nouveau monome convenablement dans le polynome courant.
        Parameters
        ----------
        m : Monome
            monome à inserer dans le polynome appelant.
        """
        b = self.localiser(m)
        m.suivant = b.suivant
        b.suivant =  m
        