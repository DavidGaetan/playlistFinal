#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 15 oct. 2014

@author: etudiant
'''

import logging
from Configuration.Arguments import argparse

def VerifcationEntier(laQuantite):

    try:
        '''
        Verification que laQuantite est bien un entier
        '''
        laBonneQuantite=int(laQuantite)
        logging.info("La quantite est bien de type entier")


        #Convertion en nombre positif

        if laBonneQuantite <=0 and laBonneQuantite >=100:
            logging.info("La Quantite qui a ete saisie est positive et 0 <= uneBonneQuantite >= 100")
            return laBonneQuantite



        #Si la Bonne Quantite est negative, la Bonne Quantite est mis en valeur absolue (c'est a dire positive)

        elif (laBonneQuantite<0 and laBonneQuantite>=-100):
            laBonneQuantite=abs(laBonneQuantite)
            logging.info("La Quantite saisie est negative elle est transformer en entier positif.")
            return laBonneQuantite



        #si non la Bonne Quantite est >-100ou < 100
        #on retourne en sortie
        else:
            logging.error("La Quantite saisie est inferieur a -100 ou superieur a 100.")
            exit(2)

    except ValueError:
        logging.error("Erreur de conversion,la Quantite est une chaine.")
        print("Il y a une erreur de saisie de Quantite, le nombre n'est pas un entier veuillez saisir un entier naturel.")
        exit(1)




def Verification ():
    '''Liste des arguments du programme'''
    Attributs=['genre'] #,'ar','sg','alb','t','r']


    ''''Boucle pour parcourir la liste des arguments saisies par l'utilisateur'''
    for arg in Attributs:
        '''On initialise un compteur d'argument par option et le pourcentage total de la playlist'''
        i,pourcentage=0,0

        if getattr(argparse, arg) is not None:
            ListeArg=getattr(argparse, arg)
            logging.info("L'option "+arg+" est bien present.")

            '''Tant qu'il y a plusieurs argument de la meme option'''
            while i<len(ListeArg):
                Argument=ListeArg[i]
                ArgumentEntier=Argument[1]

                '''On incremente le curseur'''
                i=i+1

                try:
                    '''On va donner l'entier saisie a une fonction pour la verifier'''
                    argVerif=VerifcationEntier(ArgumentEntier)
                except Exception:
                    logging.error("La fonction de verification d'un entier n'a pas fonctionner")

                try:
                    '''On rentre la saisie dans une variable qui totalise les pourcentages saisies'''
                    pourcentage+=argVerif


                    '''On verifie le le total des pourcentages saisies par l'utilisateur.'''
                    if pourcentage>100:
                        print("Votre demande est superieur a 100%, veuillez saisir un valeur dont le total ne depasse pas ce seuil!")
                        logging.info("Le programme c'est arrete car le max de pourcentage a ete atteint.")
                        exit(3)
                except Exception:
                    logging.error("Le compte des pourcentages c'est mal effectue.")

                try:
                    '''On remplace la saisir de l'utilisateur par un entier'''
                    setattr(argparse,arg,argVerif)
                except Exception:
                    logging.error("Le remplacement de la valeur entier n'a pas pu se faire.")
                    exit(4)
        else:
            logging.info("L'option "+arg+" n'est pas presente.")
