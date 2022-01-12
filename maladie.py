from operateur import *


class Maladie:
    def __init__(self, nom: str, description: str,sympto: list):
        self.nom = nom
        self.description = description
        self.sympto = sympto

    def __str__(self):
        return "{0} : {1}\nSymptôme: {2}\nTraitement: {3}\n".format(self.nom, self.description, ", ".join(self.sympto) ,self.traitement)

    def __del__(self):
        data = lire("fichier.json")
        del data["Maladie"][
            data["Maladie"].index({
                "nom" : self.nom,
                "description" : self.description,
                "traitement" : self.traitement,
                "sympto": self.sympto
            })
        ]
        ecrire("fichier.json",data)
        print("Patient supprimer avec succes !")

    def create(self):
        data = lire("fichier.json")
        data["Maladie"].append(
            {
                "nom" : self.nom,
                "description" : self.description,
                "traitement" : self.traitement,
                "sympto": self.sympto
            }
        )
        ecrire("fichier.json",data)

    def find(name: str):
        data = lire("fichier.json")
        for index,maladies in enumerate(data["Patient"]):
            for key in maladies:
                if name.lower() == key.lower():
                    nom = data["Maladie"][index]["nom"]
                    description = data["Maladie"][index]["description"]
                    sympto = data["Maladie"][index]["sympto"]
                    traitement = data["Maladie"][index]["traitement"]
                    return Maladie(nom,description,sympto,traitement)
        return None

    def update(self):
        data = lire("fichier.json")
        data["Maladie"][
            data["Maladie"].index({
                "nom" : self.nom,
                "description" : self.description,
                "traitement" : self.traitement,
                "sympto": self.sympto
            })
        ] = {
            "nom" : self.nom,
            "description" : self.description,
            "traitement" : self.traitement,
            "sympto": self.sympto
        }
        ecrire("fichier.json",data)

    def search(recherche: str=''):
        data = lire("fichier.json")
        size = len(data["Maladie"])
        for index in range(size):
            m = Maladie.find(data["Maladie"][index]["nom"])
            if recherche.lower() in m.nom.lower():
                print(m)

    