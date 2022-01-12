from typing import Dict
from operateur import *
import datetime
import json



class patient:
    def __init__(self, nom: str, prenom: str, adresse: str, age: int,  consultations = {} , numero: int=0):
        self.nom = nom.lower()
        self.prenom = prenom.lower()
        self.adresse = adresse.lower()
        self.age = age
        self.consultations = consultations
        # self.numero = numero
        if (numero == 0):
            data = lire("fichier.json")
            self.numero = data["Patient"][-1]["numero"]+1
        else:
            self.numero = numero


    def consulter(self):
        print("consultation de {} {}...".format(self.nom, self.prenom))
        print("\n")
        
        # nom= (input("Entrez le nom du patient : ")).lower()
        # prenom=(input("Entrez le prenom  du  patient : ")).lower()"
       # p1= patient(nom,prenom,"",100) 
        #if(p1.verification() == True ):
            #rt=p1.trouver() 
        consul={
                    
                    "sphere_loin":    int(input("Entrez la valeur de la sphère lointaine : ")),       
                    # "cylindre_loin":   int(input("Entrez la valeur du cylindre lointain : ")),       
                    # "axe_loin":  int(input("Entrez la valeur de l'axe lointain : ")),       
                    # "sphere_pres": int(input("Entrez la valeur de la sphère de près : ")),       
                    # "cylinfre_pres": int(input("Entrez la valeur du cylindre de près : ")),       
                    # "axe_pres": int(input("Entrez la valeur de l'axe de près : ")), 
                    # "date_analyse": str(datetime.datetime.now())

                   }
            
        #self.consultations.append(consul)
        data = lire("fichier.json")
        b = data["Patient"]
        for patient in  b:
            if((patient["numero"]==self.numero)):
                patient["consultations"][5]=consul
        # data["Patient"][0] = {
        #     "numero": self.numero,
        #     "nom": self.nom,
        #     "prenom": self.prenom,
        #     "adresse": self.adresse,
        #     "age": self.age,
        #     "consultations": self.consultations,
        # }
        ecrire("fichier.json",data)
        print(self)
        #self.update()
        


    
    def trouver(self):
        data = lire("fichier.json")
        b= data["Patient"]
        for patient in  b:
                if((patient["nom"]==self.nom) and(patient["prenom"]==self.prenom)):
                    return (patient["consultations"])
        return None


    def verification(obj):
        data = lire("fichier.json")
        b= data["Patient"]
        for patient in  b:
                if((patient["nom"]==obj.nom) and(patient["prenom"]==obj.prenom)):
                    return True
        
        return False
                      
    
    def create(self):
            data = lire("fichier.json")
            if(self.verification()==False):
                data["Patient"].append(
                    {
                        "numero": self.numero,
                        "nom" : self.nom,
                        "prenom" : self.prenom,
                        "adresse" : self.adresse,
                        "age" : self.age,
                        "consultations": {},
                        
                    }
                )
                print("patient ajouter")
                ecrire("fichier.json",data)
            else:
                   print("Erreur de creation du patient, veuillez reessayer !!")

    
    def update(self):
        # self.trouver()
        data = lire("fichier.json")
        # rt=int(self.trouver()) 
        data["Patient"][self.numero] = {
            "numero": self.numero,
            "nom": self.nom,
            "prenom": self.prenom,
            "adresse": self.adresse,
            "age": self.age,
            "consultations": self.consultations,
            
        }
        ecrire("fichier.json",data)
    

p1= patient("Abalo","za","adidogomé",18) 
p1.create()
p1.trouver()
p1.consulter()