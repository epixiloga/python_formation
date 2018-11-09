chiffre = 2
#resultat = chiffre + chiffre


# resultat = 0
# numero_etape=0
# while numero_etape <25:
#     numero_etape = numero_etape+1
#     resultat= resultat + 2
#     print("etape {0} de calcul : {1}". format (numero_etape,resultat))


# mon_tableau=["bonjour","au revoir","bonne journee"]

# for cellule in mon_tableau:
#     print(cellule)


# i=0
# j= int(input("taille du triangle"))
# while i < j:
#     print(i * "*")
#     i+=1


y= int(input("nombre de repition"))
x= int(input("taille du triangle"))

for j in range (y):
    
    for i in range (x):
        print(i * "*")
   