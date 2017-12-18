# calcul de la resistance pour un comparteur inverseur a hystéris 
def r2(Vsat,Vb,R1):
    return R1*((Vsat/Vb)-1)
print(r2(13,5,1000))