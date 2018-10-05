# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Problème 16

def SumDigits(n):
    a=2**n
    a=str(a)
    sum=0
    for i in range (len(a)):
        sum+=int(a[i])
    return sum

assert SumDigits(15)==26

print(SumDigits(1000))

#Problème 22

def NameInOrder():
    f=open("p022_names.txt",'r')
    chaine=[]
    for ligne in f:
        chaine.append(ligne)
    liste=chaine.split(',')
    sorted(liste)

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def ValueName(name):
    value=0
    for i in range(len(name)):
        j=0
        while name[i]!=alphabet[j]:
            j+=1
        value+=j+1
    return value
        
def NamesScores():
    liste=NameInOrder()
    score=0
    for i in range (len(liste)):
        score+=ValueName(liste[i])*(i+1)
    return NamesScores

print(NamesScores())

#Problème 55

def CheckPalyndrome(n):
    n=str(n)
    for i in range (len(n)):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True

def reverse(n):
    n=str(n)
    inv=''
    for i in range (len(n)):
        inv=inv+(n[len(n)-1-i])
    return int(inv)

def LychrelNumbers(n):
    nbreLychrel=0
    for i in range (1,n+1):
        somme=0
        inv=reverse(i)
        somme=inv+i
        for j in range(50):
            if CheckPalyndrome(somme)==True:
                break
            else:
                somme+=reverse(somme)
            nbreLychrel+=1
    return nbreLychrel
    
print(LychrelNumbers(10000))
    
    
    
    
    
    