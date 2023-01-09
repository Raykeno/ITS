# usr/bin/python

# Otto Hajdu, 09/01/2023
# Implémentation de l'exemple de 6 villes sans func récursive
# J'y suis allée rapidos honnetement et le code aurait pu être plus propre

from itertools import permutations
import time

sTime = time.time()

# etape 1 : chemin ou circuit hamiltonien (1 en 1 point de visite)
# On peut rajouter autant de points qu'on veut si nécessaire ou changer la liste mais elle doit garder la structure :
# [name,x,y]
dotlist = [['A',1,1],['B',2,2],['C',1,3],['D',3,2],['E',3,5],['F',7,2]]
dotlistsimple = [['A',1,1],['B',2,2],['C',1,3]]


# générer les permutations
l = list(permutations(dotlist))

S = []
i = 0
fList = []

# à fix

def recurPermu(list, S, i, fList):
    if (len(list) == 0):
        fList.append(S)
    else :
        for j in range(0,len(list)):
            S = S.append(list[j][0])
            print("i : " + str(i) +" bruh : "+ sToSTR(S)) 
            list = list[:j:]
            i = i +1      
            recurPermu(list, S, i, fList)
            
def sToSTR(S):
    res = ' '
    for i in S:
        res = res+ ' '+ i    
    return res 
  

# notre liste pour faire des prints pour plus tard
finalList = []

# Après on peut mettre nos permutations en arguments pour calculer notre cout

# On calcule le cout pour une seule permutation
def cout(permutationResult) :
    lsize = len(permutationResult)
    totalCout = distance(0, permutationResult[0][1], 0 ,permutationResult[0][2]) + distance(permutationResult[lsize-1][1],0,permutationResult[lsize-1][2],0)
    for i in range(1,lsize-1):
        totalCout = totalCout + distance(permutationResult[i][1], permutationResult[i+1][1], permutationResult[i][2],permutationResult[i+1][2])
    return totalCout
    
# On calcule tout les couts de notre liste de permutations, on l'ajoute à une liste 'finalList' qui sera notre résultat    
def allCout(permList):
    printStr = ''
    for item in permList:
        printStr = ''
        result = 0
        for point in item:
            printStr = printStr + point[0]
        result = cout(item)
        finalList.append([printStr,result])
        printStr = printStr + " : " + str(result) + "\n"
    return printStr
    
# Calcule la distance entre nos 2 points
def distance(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# Récupère la clé de l'élement qu'on veut, ici on veut le nombre pour trier la liste
def get_num(element):
    return element[1]

# Permet d'avoir un affichage correct dans le terminal 
def coolPrintList(list):
    for i in range(0, len(list)-1):
        print(list[i][0] + ' : ' + str(list[i][1]))
        


# ----------------------------------------------------------------------------------------
# main de notre programme

allCout(l) # obligé pour avoir finalList avec nos résultats
finalList.sort(reverse=True, key=get_num)
coolPrintList(finalList)
print("\nNous avons " + str(len(finalList)) + " permutations" )
eTime = time.time()
print("temps d'éxecution en secondes : " + str(eTime - sTime))

recurPermu(dotlistsimple, S, i, fList)