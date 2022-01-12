import copy
from model import patient
from model import AnalysePatient 

def serialiseur_perso(obj):
    if isinstance(obj, AnalysePatient):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = patient
        return {
                "__class__": "AnalysePatient",
                "sphere_loin"   :  obj.sphere_loin,
                "cylindre_loin" : obj.cylindre_loin,
                "axe_loin":      obj.axe_loin,
                "sphere_pres":   obj.sphere_pres,
                "cylinfre_pres": obj.cylinfre_pres,
                "axe_pres":      obj.axe_pres,
                "diagnostic": obj.z,
                "__parent__":    obj_cpy}
    
    if isinstance(obj, patient):
        return {"__class__": "patient",
                "id":   obj.id,
                "nom":  obj.nom,
                "age":  obj.age,
                "sexe": obj.sexe}

