# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from numpy import *
from pylab import *
##Script émettant un cos d'amplitude 10, le rend unitaire puis cherche la frequence
##T=1
##Te=T/1000
##Ne=1024
#te=linspace(0,1,1000)
#wp=200
#S=10*sin(wp*te)
#plot(te,S)
#Signal=S/maxSign)
#plot(te,Signal)
#S1=list(Signal)
##t0=S1.index(0.8)
#valid=True
#for i in range(len(te)):
#    if S1[i]>0.5 and S1[i]<0.55 and valid:
#        r=i
#        valid=False
#        
#R=[]
#for i in range(len(te)):
#    if S1[i]<=1.05*S1[r] and S1[i]>=0.95*S1[r]:
        R.append(i)
def NettoyageListe(L):
    Rf=[L[0]]
    l=len(L)
    for i in range(l-1):
        if L[i+1]-L[i]>50:
            Rf.append(L[i+1])
    return(Rf)
Rf=NettoyageListe(R)
distance=te[Rf[2]]-te[Rf[0]]
Freq=1/distance
print(Freq)


def FrequencePWM(S,Te):
    """S array d'un signal, on le rend unitaire et on cherche sa frequence avec la distance entre deux motifs,Te temps d'acquisition"""
    te=linspace(0,Te,1000) #Faire attention a vérifier les conditions de Shannon-Nyquist
    Signal=S/max(S)
    plot(te,S)
    S1=list(Signal) #Pour avoir une liste pour la recherche des points
    valid=True #Condition pour chercher le premier point
    Liste=[] #Liste qu'on remplira des points alignés
    for i in range(len(te)):
        if S1[i]>0.5 and S1[i]<0.55 and valid:
            r=i
            valid=False
    for i in range(len(te)):
        if S1[i]<=1.05*S1[r] and S1[i]>=0.95*S1[r]:
            Liste.append(i)
    ListeFiltree=NettoyageListe(Liste) #Crée la liste filtrée pour virer les premiers points trop proches
    distance=te[ListeFiltree[2]]-te[ListeFiltree[0]] #Distance entre les deux points alignés
    Freq=1/distance #Par définition
    return(Freq)

def NettoyageCarre(S,n):
    """S array d'un signal, on va faire une moyenne par glissement pour lisser le signal"""
    Signal=list(S)  
    Longueur=len(S)
    filtree=np.zeros(Longueur)
    if Longueur%n!=0
        S.pop()
        return(NettoyageCarre(S)
    elif Longueur%n==0: 
        for i in range(Longueur/b):
            Moyenne=Signal[i*3]
            for k in range(n):
                Moyenne=MoyenneSignal[i*3+k]
            Moyenne=Moyenne/n
                for j in range(n):
                filtree.append(Moyenne)
    return(filtree)
def Filtragetot(S):
    filtree=S
    Longueur=len(S)
    for i in range(3,5):
        filtreeNettoyageCarre(filtree)
       