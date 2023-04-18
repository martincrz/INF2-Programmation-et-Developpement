#C:\Users\marti\PycharmProjects\pythonProject

import sqlite3

def main_exo3():
    fichier_bdd = "BDD-exo4.sqlite"
    connexion = sqlite3.connect(fichier_bdd)
    curseur = connexion.cursor()

    try:
        print("# Récupérer la liste des clients")
        curseur.execute('SELECT * FROM client ')
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")

        print("# Récupérer la liste des numéros de téléphone pour le client numéro 1")
        curseur.execute('SELECT numero FROM numero_telephone INNER JOIN client ON client.id=numero_telephone.client_id WHERE client.id=1 ')
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")

        print("# Récupérer la liste des noms et prénoms des clients ainsi que le nom de leur ville")
        curseur.execute('SELECT client.nom, client.prenom, ville.nom FROM ville INNER JOIN client ON client.ville_id=ville.id')
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")
        #SELECT c.nom, c.prenom, v.nom FROM client AS c INNER JOIN ville AS v ON c.ville_id=v.ID

        print("#Récupérer la liste des noms et prénoms des clients pour le département 60")
        curseur.execute('SELECT client.nom, prenom FROM client INNER JOIN ville ON client.ville_id=ville.id WHERE ville.code_departement=60')
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")

        #ATTENTION UN CLIENT A PLUSIEURS NUMEROS, L'UN PEUT ETRE DEMARCHE L'AUTRE NON, FAIRE UNE REQUETE AVEC INNER JOIN MARCHERAIT PAS
        print("Récupérer liste des clients jamais démarchés")
        curseur.execute('SELECT c.nom, c.prenom FROM client AS c WHERE c.id NOT IN (SELECT n.client_id FROM numero_telephone AS n WHERE est_demarche=TRUE)')
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")

        print("Récupérer la liste des noms et prénoms et numéros de téléphone des clients dont l'opérateur est SuperTelecom")
        curseur.execute("SELECT c.nom, c.prenom, numero FROM client AS c INNER JOIN numero_telephone ON c.id=client_id INNER JOIN operateur ON operateur_id=operateur.id WHERE operateur.nom='SuperTelecom' ")
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")
        #pour avoir la liste des clients des autres opérateurs, il faut enlever la condition WHERE

        print("Récupérer la liste des noms et prénoms des clients avec le nom de leur opérateur et leur numéro de téléphone.\nOn veut également récupérer les numéros de téléphone pour lesquels l'opérateur n'est pas connu.")
        curseur.execute('SELECT client.nom, prenom, operateur.nom, numero FROM client INNER JOIN numero_telephone ON client.id=numero_telephone.client_id INNER JOIN operateur ON numero_telephone.operateur_id=operateur.id ')

        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")
        print("#IL FAUT RAJOUTER LA LISTE DES NUMEROS POUR LESQUELS L OPERATEUR N EST PAS CONNU")
        curseur.execute( "SELECT c.nom, c.prenom,n.numero, o.nom FROM client AS c INNER JOIN numero_telephone AS n ON c.ID=n.client_id LEFT JOIN operateur AS o ON o.ID=n.operateur_id")
        for enregistrement in curseur:
            print(enregistrement)
        print("\n\n")


        print("Ajouter une ville")
        curseur.execute("INSERT INTO ville VALUES (NULL, 'Compiegne', 60, 60200, 7896, 1000000)")
        print("Ville ajoutee")
        print("\n\n")

        print("Supprimer la ou les villes dont le code postal est 60521")
        curseur.execute("SELECT * FROM ville WHERE code_postal=60521 ")
        for enregistrement in curseur:
            print(enregistrement)
        curseur.execute("DELETE FROM ville WHERE code_postal=60521")
        print("ville(s) supprimee(s)")
        print("\n\n")

        print("Marquer comme démarché le numéro de telephone '03.11.22.33.44'")
        curseur.execute("UPDATE numero_telephone SET est_demarche=True WHERE numero='03.11.22.33.44' ")
        print("Numero maintenant demarque")
        print("\n\n")

        print("Changer l'opérateur du numéro 03.11.22.33.44 pour l'opérateur d'id 4. Que se passe-t-il si cet opérateur n'existe pas ?")
        curseur.execute("UPDATE numero_telephone SET operateur.id=4 WHERE numero='03.11.22.33.44'")
        print("\n\n")

        print("Changer l'opérateur du numéro 03.11.22.33.44 pour l'opérateur SuperTelecom . Utiliser une sous-requête.")
        curseur.execute("UPDATE numero_telephone SET operateur.id=(SELECT id FROM operateur WHERE nom='SuperTelecom') WHERE numero='03.11.22.33.44' ")
        print("\n\n")

        print("Supprimer le client numéro 1.")
        curseur.execute("DELETE FROM client WHERE ID=1")
        print("\n\n")

        connexion.commit()
        curseur.close()
        connexion.close()

    except FileNotFoundError:
        print("Fichier introuvable")


if __name__=='__main__':
    main_exo3()

