'''
Created on 22 nov. 2014

@author: david
'''
import logging
import io

'''Pour une extension en M3U'''
def CreationM3u(nom, ext, result):
    logging.info("Ecriture du fichier M3U")
    fichier=io.open(nom + "." + ext,'w')
    ''' ecriture de chaque musiques dans la liste result '''
    for row in result:
            fichier.write("#EXTINF:" + str(row[3]) + ", " + row[1] + " - " + row[2] + "\n")
            fichier.write(row[4] + "\n\n")
    fichier.close()
    logging.info("Ecriture du fichier M3U TERMINER")








''' Pour une extension en XSPF '''
def CreationXspf(nom, ext, result):
    logging.info("Ecriture du fichier XSPF")
    fichier=io.open(nom + "." + ext,'w')
    fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ nom +"</title>\n"+
                       "\t<trackList>\n")
    ''' Pour chaque elements de la liste, on ajout cet element dans le fichier de playlist '''
    for row in result:
            fichier.write("\t\t<track>\n\t\t\t<location>file://"+ row[4] +"</location>\n"+
                               "\t\t\t<title>"+ row[0] +"</title>\n"+
                               "\t\t\t<creator>"+ row[1] +"</creator>\n"+
                               "\t\t\t<album>"+ row[2] +"</album>\n"+
                               "\t\t\t<duration>"+ str(row[3]) +"</duration>\n"+
                               "\t\t</track>\n")
    fichier.write("\t</trackList>\n</playlist>")
    fichier.close()
    logging.info("Ecriture du fichier XSPF Terminer")






''' Pour une extension en PLS '''
def CreationPls(nom, ext, result):
    logging.info("Ecriture du fichier PLS")
    i=1
    fichier=io.open(nom + "." + ext,'w')
    fichier.write("[playlist]\n\n")
    for row in result:
        fichier.write("File"+ str(i) +"="+ row[4] +"\n")
        fichier.write("Title"+ str(i) +"="+ row[0] + "\n")
        fichier.write("Length"+ str(i) +"="+ str(row[3]) + "\n\n")
        i+=1
    fichier.write("NumberOfEntries="+ str(len(result)) +"\nVersion=2")
    fichier.close()
    logging.info("Ecriture du fichier PLS Terminer")