import copy
from model import patient
from model import AnalysePatient 

def deserialiseur_perso(obj_dict):
        if "__class__" in obj_dict:
            if obj_dict["__class__"] == "patient":
                obj={}
                obj.nom = obj_dict["nom"]
                obj.age = obj_dict["age"]
                obj.sexe = obj_dict["sexe"]
                return obj
        #return objet
    
# def deserialiseur_perso(obj_dict):
#     if "__class__" in obj_dict:
#         if obj_dict["__class__"] == "Playlist":
#             obj = Playlist(objet["nom"])
#             obj.musiques = objet["musiques"]
#             return obj
#     return objet
        
        

        
