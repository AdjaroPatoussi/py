import json
from serialisation import serialiseur_perso
from model import patient
from model import AnalysePatient 
from deserialisation import deserialiseur_perso

p1= patient(1,"ed",18,"M") 
p2= AnalysePatient(2,"ed",18,"M",1,2,3,4,7,6)
p3= AnalysePatient(3,"ed",18,"M",0,0,0,0,1,0)

liste_patient = []
liste_patient.append(p1)
liste_patient.append(p2)
liste_patient.append(p3)

with open('Test.json', 'w', encoding='utf-8') as f:
    json.dump(liste_patient, f, indent=4, default=serialiseur_perso)


# On crée un objet vide.
list={}

# On le peuple à l'aide du fichier JSON.
with open("test.json", "r", encoding="utf-8") as fichier:
   list = json.load(fichier, object_hook=deserialiseur_perso)
   #list=json.load(fichier)

# for a in list:
#     print (deserialiseur_perso(a))"