#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Configuration.Arguments import Arguments
from Configuration.ConfigurationFichierLogs import LoggingConf

from Gestion.baseDeDonnee import ConnectionBDDMusique
from Gestion.Calcul import CalculPourcentage
from Gestion.GenerationPlaylist import CreationM3u,CreationPls,CreationXspf

from Verification.VerificationEntier import Verification,VerifcationEntier
import logging

''' execution de la methode de controle des saisies de l utilisateur '''

logging.info("Debut du Programme")
logging.info("Importation de la configuration du fichier")
''' création du fichier de logs '''
LoggingConf()

args = Arguments()

logging.info("La saisie utilisateur est : "+str(args))

logging.info("verification entier du temps de la playliste")
VerifcationEntier(args.temps)


logging.info("si argument est non null, ici on verifi le format du pourcentage")
for unArg in ['genre','artiste','album', 'titre']:
    '''si argument est non null'''
    if getattr(args, unArg) is not None:
        logging.info("Vérification du format du pourcentage")
        CalculPourcentage(getattr(args, unArg))


logging.info("recupération des données ")
(args)
playlist = Playlist(args)



logging.info("génération de la playlist selon le format choisi")
if (args.formatfichier =='m3u'):
    creationFichierm3u(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')
if(args.formatfichier =='xspf'):
    creationFichierxpsf(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')
if(args.formatfichier =='pls'):
    creationFichierpls(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')