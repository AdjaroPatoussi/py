

def deserialiseur_perso(obj_dict):
    if "__class__" in obj_dict:
        if obj_dict["__class__"] == "Playlist":
            obj = Playlist(objet["nom"])
            obj.musiques = objet["musiques"]
            return obj
    return objet

    
    obj = AnalysePatient(objet["id"])
                