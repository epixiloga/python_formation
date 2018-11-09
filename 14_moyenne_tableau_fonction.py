
def moyenne(tab):
    somme=0
    for i in tab:
        somme=somme+i
    return somme/len(tab)

values=[10, 2, 8, 99, 502, 4, 2, 1, 4, 13]
print(moyenne(values))


def moyenne_version_while(tab):
    somme=0
    i=0
    while i < len(tab):
        somme=somme+tab[i]
        i+=1
    return somme/len(tab)


