

def solde(prix):
    taux=2
    nouveau_prix=prix*(1-taux)
    return nouveau_prix

resultat = solde(10)
print(resultat)
#print (taux)

# taux n'est plus dispo dans le programme principal car il a ete cree dans la fonction "solde"