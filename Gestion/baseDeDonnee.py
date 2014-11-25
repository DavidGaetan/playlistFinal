'''
Created on 5 nov. 2014

@author: etudiant
'''

import sqlalchemy
import logging

#importation de sqlalchemy
'''déclaration de la connexion'''
engine = sqlalchemy.create_engine('postgresql://d.gentric:d@vd@v44ed0310@172.16.99.2:5432/bddplaylist')
''' connexion'''
conn = engine.connect()

'''déclaration
initialisation des metadata
'''
metadata = sqlalchemy.MetaData()
logging.info("Création de la base sqlalchemy ")
'''Création de sqlalchemy de la bas'''
morceaux = sqlalchemy.Table('morceaux', metadata,
                                sqlalchemy.Column('id', sqlalchemy.String, primary_key = True),
                                sqlalchemy.Column('titre', sqlalchemy.String),
                                sqlalchemy.Column('album', sqlalchemy.String),
                                sqlalchemy.Column('artiste', sqlalchemy.String),
                                sqlalchemy.Column('genre', sqlalchemy.String),
                                sqlalchemy.Column('sousgenre', sqlalchemy.String),
                                sqlalchemy.Column('duree', sqlalchemy.Integer),
                                sqlalchemy.Column('format',sqlalchemy.String),
                                sqlalchemy.Column('polyphonie',sqlalchemy.Integer),
                                sqlalchemy.Column('chemin',sqlalchemy.String))
'''affiche le contenu de la table morceaux'''
logging.info("Création de la requete")
    
requette = sqlalchemy.select([morceaux]).where(morceaux.c.titre == 'introspect')
logging.info("Execution de la requete")
result = conn.execute(requette)

return result