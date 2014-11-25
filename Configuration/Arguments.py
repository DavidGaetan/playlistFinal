#!/usr/bin/python3
# -*- coding: utf-8 -*-



import argparse
import logging

def Arguments():
    parser = argparse.ArgumentParser()

    '''Arguments obligatoire'''
    parser.add_argument("temps", help="informer la duree en minutes",type=int)
    parser.add_argument("nom", help="indiquer le nom du fichier de sortie")
    parser.add_argument("format", choices=['m3u', 'xspf', 'pls'], help="Choisir entre le format M3U, XSPF ou PLS ")
    
    '''Arguments optionnel'''
    parser.add_argument("-g", "--genre",action='append',nargs=2, help="indiquer le genre")
    parser.add_argument("-a", "--artiste",action='append', nargs=2, help="indiquer l'artiste")
    parser.add_argument("-A", "--album",action='append', nargs=2, help="indiquer l'album")
    parser.add_argument("-t", "--titre",action='append', help="indiquer le titre")
    parser.add_argument("-m", "--marge",action='append', help="marge supplementaire a ajoute a la duree",type=int)
    parser.add_argument("-sg","--sousGenre", action='append', help="sous genre possible")
    parser.add_argument("-r", "--recherche", help="recherche selon une expression")


    args=parser.parse_args()

    ''' On affiche les arguments obligatoire'''
    logging.info('----------INFO DES VALEURS des Arguments obligatoire---------')
    logging.info('le temps total de la playlist est de :'+str(args.temps))
    logging.info('Le nom de la playlist est :'+args.nom)
    logging.info('Le format de sortie est :'+args.format)