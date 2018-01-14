def construire_arbre(dict, noeud):
    if len(noeud.enfant) == 0:
        return noeud
    aTrouver = list(noeud.enfants)
    noeud.enfant.clear()
    for e in aTrouver:
        noeud.enfant.append(dict[e])
        aPlacer.pop(e)


class Programme:
    def __init__(self, nom, poids):
        self.enfants = []
        self.parents = []
        self.nom = nom
        self.poids = poids


aPlacer = dict()

with open("input.txt") as progs:
    for line in progs:
        line = line.split()
        prog = Programme(line[0], int(line[1][1:-1]))
        if len(line) > 2:
            for i in range(3, len(line)):
                if line[i][-1] == ',':
                    line[i] = line[i][:-1]
                prog.enfants.append(line[i])
        aPlacer[prog.nom] = prog

