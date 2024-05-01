#################################################
# Identifiant aiguille Ax						#
# Adresse DCC yy								#
# 01 mai 2024									#
#################################################
import time
class aiguille():
    #moteur_1 = bool(0) , moteur droit
    #moteur_2 = bool(0) , moteur courbe
    #droit = bool(0) et courbe = bool(1)
    #dcc_ad = hex(0F) = (15d)
    def __init__(self, identif, etat, dcc_ad):
        self.identif = identif
        self.etat = etat
        self.dcc_ad = dcc_ad
    # Cette fonction __init__ prend un argument très important: self. Ce mot-clef désigne l’objet lui-même.
    def mettre_droit(self):
        moteur_1 = bool(1)
        print('d')
        time.sleep(0.150)
        moteur_1 = bool()
        self.etat= bool(0)
        pass # 500ms max
    def mettre_courbe(self):
        moteur_2 = bool(1)
        print('c')
        time.sleep(0.150)
        moteur_2 = bool()
        self.etat= bool(1)
        pass # 500ms max
    pass

if __name__ == '__main__':
    Aig_0 = aiguille("A0", bool(0), hex(15))
    print(Aig_0.identif, Aig_0.etat, Aig_0.dcc_ad)
    Aig_0.mettre_courbe()
    print(Aig_0.etat)
    Aig_0.mettre_droit()
    print(Aig_0.etat)
    Aig_0.mettre_courbe()
    print(Aig_0.etat)

