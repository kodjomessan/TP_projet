from Adresse import Adresse
from Achat import Achat
from Aliment import Aliment
from Alcool import Alcool
from Client import Client
from Commercant import Commercant
from Facture import Facture
from GestionGrossiste import GestionGrossiste
from Grossiste import Grossiste
from Livraison import Livraison
from Particulier import Particulier
from Produit import Produit
from Promotion import Promotion
from Stock import Stock

if __name__ == "__main__":
    # Création d'un stock
    stock = Stock()
    
    # Création de produits
    produit1 = Aliment("ALI001", 40, 12.5, "allégé")  # TVA 5.5%
    produit2 = Alcool("ALC002", 50, 17.8)  # TVA 20%
    
    # Ajout des produits au stock
    stock.ajouter_produit(produit1)
    stock.ajouter_produit(produit2)
    stock.approvisionner_produit(produit1, 50)
    stock.approvisionner_produit(produit2, 20)
    print(stock)
    
    # Création d'une adresse
    adresse_client = Adresse(31, "Rue de la Curdy", "Rumilly", 74150, "")
    
    # Création d'un client
    client1 = Client("Bouzagou", "Fatima", adresse_client, 26102001)
    print(client1)
    
    # Création d'achats
    achat1 = Achat(client1, produit1, 10)
    achat2 = Achat(client1, produit2, 5)
    
    # Génération d'une facture
    facture = Facture(client1, [achat1, achat2])
    print(facture)
    
    # Création et test d'une gestion du grossiste
    gestion = GestionGrossiste("Gestion des ventes et des stocks")
    print(gestion)
    
    # Création d'un grossiste
    adresse_grossiste = Adresse(10, "Rue de la Mairie", "Le Bourget-du-Lac", 73370, "Entrepôt Central")
    grossiste = Grossiste("SuperKF", adresse_grossiste)
    print(grossiste)
    
    # Ajout du client au grossiste
    grossiste.ajouter_client(client1)
    
    # Création d'une livraison
    livraison = Livraison(stock, [(produit1, 30), (produit2, 10)])
    print(livraison)
    livraison.effectuer_livraison()
    
    # Création d'une promotion
    promo = Promotion(produit1, 10)  # Réduction de 10%
    print(promo)
    promo.appliquer_promotion()
    
    # Affichage final du stock
    print(stock)
