'''
Created on 4 nov. 2014

@author: etudiant
'''

from Configuration.Arguments import argparse

def CalculPourcentage():
#
#methode qui créer une liste integrant les new %
#exemple:  rock 20 reock 90 rock 80
#          mis a 100%
#          rock 10.53 reock 47.7 rock 42.4
#          total=100.63


    Attributs=['genre','artiste','album','titre','marge','sousGenre','recherche']

    for arg in Attributs:

        nbarg,i,pourcentage=0,0,0

        ''' parcours et recuperation de l'argument [1] de temps '''
        if getattr(argparse, arg) is not None:
            '''liste de recupération des 2 argumant exemple:'rock' et '20'  '''
            ListeArg=getattr(argparse, arg)
            #nbarg = count(len(ListeArg))

            '''création de la liste de recuperation des arguments de pourcentages (deuxieme argumant '20')'''
            listeDesPourcentage = []
            '''Tant qu'il y a plusieurs argument de la meme option'''
            while i < len(ListeArg):
                Argument=ListeArg[i]
                '''récupération de la valeur de l'entier du pourcentage'''
                ArgumentEntier = Argument[1]
                '''ajout de l'entier pourcentage dans la list qui rassemble la totaliter des pourcentage de la commande'''
                listeDesPourcentage.extend([ArgumentEntier])
                '''On incremente le curseur'''
                i = i + 1

        '''ici on compte le nombre d'itemes dans la liste '''
        nbarg = {ArgumentEntier: listeDesPourcentage.count(ArgumentEntier) for ArgumentEntier in set(list)}

        '''ici on fait la somme des itemes de la liste des pourcentages'''
        sumlisteDesPourcentage=sum(listeDesPourcentage)

        '''declaration de la liste pour l'arriver des nouveaux pourcentage remis a une echelle totale de 100%'''
        listeDesNewPourcentage = []


        '''si la somme est != 100%'''
        if sumlisteDesPourcentage != 100 :
            '''methode de remise la l'échelle des 100% total'''
            a, x = 0,0
            a = sumlisteDesPourcentage/100
            '''ajout a la liste pour chaque new pourcentage'''
            
            for ArgumentEntier in listeDesPourcentage
            #a*listeDesPourcentage[x]=unNewPourcentage
            unNewPourcentage=listeDesPourcentage
            listeDesNewPourcentage.extend([unNewPourcentage])
            '''incrémantation de x++'''
            x= x + 1
            return 

        '''a utiliser en debut'''
        if sumlisteDesPourcentage >= 100 and arg is None :
            'leNbDArgs' = count(arg) "compte le nombre de arg"
            'porcentages'=arg+arg+argnone
            p/c =
            arg+arg+p