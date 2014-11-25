'''
Created on 18 nov. 2014

@author: etudiant
'''
import sqlalchemy
import random
from Gestion.baseDeDonnee import morceaux, engine as connect

'''  '''
argumentSaisie = ['genre','artiste','album','titre']

'''Définition de la playlist'''
playlist =[]

'''Creation de la requete et récupérer des données dans la BDD en fonction de la saisie de l'utilisateur '''
def recupererDonnees(args):
    for attribut in argumentSaisie:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                
                '''si genres est saisie  une ou plusieur foi'''
                if (attribut == 'genre'):
                    RecuperationDonnees = sqlalchemy.select([morceaux]).where(morceaux.c.genre == argument[0])
                '''si artiste est saisie  une ou plusieur foi'''
                if (attribut == 'artiste'):
                    RecuperationDonnees = sqlalchemy.select([morceaux]).where(morceaux.c.artiste == argument[0])
                '''si album est saisie  une ou plusieur foi'''
                if (attribut == 'album'):
                    RecuperationDonnees = sqlalchemy.select([morceaux]).where(morceaux.c.album == argument[0])
                '''si le titre ai saisie une ou plusieur foi'''
                if (attribut== 'titre'):
                    RecuperationDonnees = sqlalchemy.select([morceaux]).where(morceaux.c.titre == argument[0])

                ''' connection et execution de la requète'''
                recuperation = connect.execute(RecuperationDonnees)
                '''Insertion des données récuperées dans un list'''
                recuperation = list(recuperation)
                '''Melange les musiques'''
                random.shuffle(recuperation)



                #Rajoute une liste au 3eme rang de la liste argument
                argument.insert(2,[])
                ''''i et durée à 0 pour la prochaine boucle for'''
                i, duree = 0,0




                ''' Remplire la playlist s'l reste assez de temps pour une ou plusieurs musiques '''
                for champBDD in recuperation:
                    #Ajoute la durée de la musique à la durée de la playlist en cours de créationn
                    duree += champBDD[5]
                    ''' ajout de d'une musique si duree < temps de la playlist'''
                    if(duree < argument[1]*60):
                        '''Insertion de la musique dans la playlist'''
                        argument[2].insert(i, champBDD)
                        i += 1
                    #Sinon suppression de la durée de la musique anciennement ins
                    else:
                        duree -= champBDD[5]




'''Génération de la liste pour la playlist'''
def generationPlaylist(args):
    i = 0
    for attribut in argumentSaisie:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                # Pour chaque musique dans la playlist on insére le titre, l'artiste, l'album, le format et le chemin
                for musique in argument[2]:
                    playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    '''Mélange les musiques aléatoirement'''
    random.shuffle(playlist)



def Playlist(args):
    '''Définition de la duree en cours de la playlist généré et initialisation à 0'''
    duree = 0
    #Pour chaque ligne de playlist on va ajouter le temps de la musique à la duree
    for musique in playlist:
        duree += musique[3]

'''Si la duree de la musique est inférieur à la durée demandée par l'utilisateur,'''
#une requête va permettre d'aller chercher des musiques alétoirement dans la BDD
    if(duree < args.temps*60):
        select_morceaux = sqlalchemy.select([morceaux])
        resultat = connect.execute(select_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)

    #Initialisation de i au nombre de ligne de la liste playlist
    i=len(playlist)

    #Pour chaque ligne de résultat
    for musique in resultat:
        #Ajout de a la durée de la ligne (musique) à la durée de la playlist en cours de création
        duree += musique[5]
        #Si la durée de la playlist en cours de création, on va insérer la ligne dans la liste playlist
        if(duree < args.temps*60):
            playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        #Sinon on enlève la durée de la ligne à la durée de la playlist en cours de création
        else:
            duree -= musique[5]

    #On va retourner la playlist créée
    return playlist