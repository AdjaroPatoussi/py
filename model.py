class patient:
    def __init__(self, id, nom,age,sexe):
        self.id= id
        self.nom= nom
        self.age=age
        self.sexe=sexe


class AnalysePatient(patient):
    
    z  = dict()
    def __init__(self,id,nom,age,sexe, sphere_loin, cylindre_loin, axe_loin, sphere_pres, cylinfre_pres, axe_pres):
        patient.__init__(self, id, nom,age,sexe)
        self.sphere_loin =  sphere_loin
        self.cylindre_loin= cylindre_loin
        self.axe_loin=axe_loin
        self.sphere_pres=sphere_pres
        self.cylinfre_pres=cylinfre_pres
        self.axe_pres=axe_pres
        self.z=self.resultat()


    def sphere_analyse(self):
        if (self.sphere_loin <0)and (self.sphere_pres < 0):
            return("myopie")
        elif (self.sphere_loin ==0)and (self.sphere_pres == 0):
            return("Oeil normal")

        elif (self.sphere_loin ==10 )and (self.sphere_pres == 10):
            return("le patient est Aveugle")
        else:
            return("hypermetropie")


    def astigmatisme_analyse_pres (self):
        if (self.cylinfre_pres == 0) and (self.axe_pres == 0):
            return("aucune presence d'astigmatisme")
        else:
            return("presence d'astigmatisme: ", self.cylinfre_pres, "l'angle de deformation est ", self.axe_pres )



    def astigmatisme_analyse_loin(self):
        if (self.cylindre_loin == 0) and (self.axe_loin == 0):
            return("aucune presence d'astigmatisme")
        else:
            return("presence d'astigmatisme: ", self.cylindre_loin, "l'angle de deformation est ", self.axe_loin )

    def resultat(self):

        d = dict()
        d['AnalyseSphere'] = self.sphere_analyse()
        d['AstigmatismePres'] = self.astigmatisme_analyse_pres()
        d['AstigmatismeLoin'] = self.astigmatisme_analyse_loin()
        return d
        
        








