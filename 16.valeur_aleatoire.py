import random

aleatoire = random.randint(0,100)
x= int(input("nombre de tentative"))
 

valeur_proposee=[]
valeur = int(input("entrez une valeur  "))
for i in range(x):
    valeur_proposee.append(valeur)
    
    if valeur < aleatoire:
            valeur = int(input("entrez une valeur plus grande  ")) 
            # valeur_proposee.append(valeur)
            
        
    elif valeur > aleatoire:
            valeur = int(input("entrez une valeur plus petite ")) 
            # valeur_proposee.append(valeur)
    
    else:
            print("bravo vous avez trouve la valeur")



print("desole vous atteint le nombre maximum de tentatives et le nombre mystere est {0}".format(aleatoire))
print(valeur_proposee)



######### avec while
# i=0
# gagne=False
# while i < x:
#     valeur = int(input("entrez une valeur  ")) 
#     if valeur>aleatoire:
#         print("entrez une valeur plus petite")
#     elif valeur < aleatoire:
#             valeur = int(input("entrez une valeur plus grande  ")) 
#     else:
#             print("bravo vous avez trouve la valeur")
#             gagne=True
#             break
#     i+=1
# if gagne == False:
#     print("desole vous atteint le nombre maximum de tentatives {0}".format(x))


    