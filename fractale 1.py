# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:24:37 2020

@author: landr
"""

import matplotlib.pyplot as plt
import random

p = random.uniform(0,1)
if 0<= p <=0.1 :
     abscice = [0]*30000 
     abscice[0]=0.5
     ordon = [0]*30000
     ordon[0]=0
     for i in range (29999):
         abscice[i+1]=0.05*abscice[i]
         ordon[i]=0.6*ordon[0]
if  0.1<= p <=0.2 :
        abscice = [0]*30000 
        abscice[0]=0.5
        ordon = [0]*30000
        ordon[0]=0
        for i in range (29999):
            abscice[i]=0.05*abscice[0]
            ordon[i+1]=(-0.5)*ordon[i]+1
if  0.2 <= p <=0.4 :
        abscice = [0]*30000 
        abscice[0]=0.5
        ordon = [0]*30000
        ordon[0]=0
        for i in range (29999):
            abscice[i+1]=0.46*abscice[i] -0.32*ordon[i]
            ordon[i+1]=0.39*abscice[i]+(-0.38)*ordon[i]+0.6
if  0.4 <= p <=0.6 :
        abscice = [0]*30000 
        abscice[0]=0.5
        ordon = [0]*30000
        ordon[0]=0
        for i in range (29999):
            abscice[i+1]=0.47*abscice[i]-0.15*ordon[i]
            ordon[i+1]=0.17*abscice[i]+0.42*ordon[i]+1.1
if  0.6 <= p <=0.8 :
        abscice = [0]*30000 
        abscice[0]=0.5
        ordon = [0]*30000
        ordon[0]=0
        for i in range (29999):
            abscice[i+1]=0.43*abscice[i]+0.28*ordon[i]
            ordon[i+1]=(-0.25)*abscice[i]+0.45*ordon[i]+1
if  0.8 <= p <=1 :
        abscice = [0]*30000 
        abscice[0]=0.5
        ordon = [0]*30000
        ordon[0]=0
        for i in range (29999):
            abscice[i+1]=0.42*abscice[i]+0.26*ordon[i]
            ordon[i+1]=(-0.35)*abscice[i]+0.31*ordon[i]+0.7
ax=plt.gca()
ax.set_xticks([])
ax.set_yticks([]) 
plt.plot(abscice,ordon,'b')
plt.show() 
            
             
              
    
        
    
        
        
    
