class Node:                                     # Class Node

    def __init__(self, data):                   # Constructor for Node
        self.leftnode = None                    # Setter instance variabel leftnode til ingen verdi
        self.rightnode = None                   # Setter instance variabel rightnode til ingen verdi
        self.value = data                       # Setter instance variabel value til verdien mottatt i parameteren data

class Tree:                                     # Class Tree
    def __init__(self):                         # Constructor for Tree
        self.root = None                        # Lage et tomt tree ( starten på treet )

    def printTree(self):                        # Class Method printTree. Brukes til å sjekke om strukturen er tom. parameter inn er et objekt
        if(self.root != None):                  # Hvis treet (self root) ikke er tomt
            self._printTree(self.root)          # Kall Method _printTree og sender med objekt. 

    def _printTree(self, node):                 # Class Method _printTree Skriver ut alle noder i tre. Parameter inn er er self og et objekt
        if(node != None):                       # Hvis parameter node ikke er None
            self._printTree(node.leftnode)      # Kall Method _printTree og sender med objekt node.leftnode.
            print(str(node.value) + ' ')        # Skriv ut string variant av node.value og en space.
            self._printTree(node.rightnode)     # Kall Method _printTree og sender med objekt node.rightnode.

    def add(self, data):                        # Class Method add. Brukes til å sjekke om strukturen er tom, og eventuelt lage tre. parameter inn er self og data
        if(self.root == None):                  # Hvis treet (self root) er tomt
            self.root = Node(data)              # Lag node med root.value lik data fra parameter
        else:                                   # Hvis treet (self root) ikke er tomt
            self._add(data, self.root)          # Kall Method self._add med parameter data og peker til root i tre

    def _add(self, data, node):                 # Class Method _add. Btukes til å legge til noder i tre under root. Parameter inn er self, data til node og et objekt| 
        if(data < node.value):                  # Hvis parameter data er mindre enn value i noden.
            if(node.leftnode != None):          # Hvis node.leftnode ikke er None
                self._add(data, node.leftnode)  # Kall Method _add med parameter data og node.leftnode
            else:                               # Hvis node.leftnode er None
                node.leftnode = Node(data)      # Lag ny Node og legg inn som node.leftnode
        else:                                   # Hvis parameter data er større enn value i noden.
            if(node.rightnode != None):         # Hvis node.rightnode ikke er None
                self._add(data, node.rightnode) # Kall Method _add med parameter data og node.rightnode
            else:                               # Hvis node.rightnode er None
                node.rightnode = Node(data)     # Lag ny Node og legg inn som node.rightnode


if __name__ == '__main__':                      # Hvis modul er main modul https://docs.python.org/3/library/__main__.html
    tree = Tree()                               # Lager et Tree men navn tree
    
    tall=1                                      # Lokal variabel tall settes til 1
    while tall !=0:                             # Så lenge variabel tall ikke er lik 0
        tall = int(input("Tast inn et tall, avslutt med 0: "))  # Be bruker taste inn et tall og avslutte med 0. Legg input i varabel tall
        if tall != 0:                           # Hvis tall ikke er 0
            tree.add(tall)                      # Kall metode add for å legge ny node i treet

    tree.printTree()                            # Kall metode tree.printTree for å skrive ut tre



Pyton binarytree Modul
# https://binarytree.readthedocs.io/en/latest/
# pip install binarytree

from binarytree import build

if __name__ == '__main__':                      # Hvis modul er main modul
    tall=1                                      # Lokal variabel tall settes til 1
    liste=[]                                    # Lokal variabel list type list opprettes tom
    while tall !=0:                             # Så lenge variabel tall ikke er lik 0
        tall = int(input("Tast inn et tall, avslutt med 0: "))  # Be bruker taste inn et tall og avslutte med 0. Legg input i varabel tall
        if tall != 0:                           # Hvis tall ikke er 0
            liste.append(tall)                  # Legger verdi tall til i liste

    tree = build(liste)                         # Bygger tree med metode build fra usortert liste
    print(tree)                                 # Skriver ut tree
    sortert = sorted(liste)                     # Sorterer liste
    sortedTree = build(sortert)                 # Bygger tree med metode build fra sortert liste
    print(sortedTree)                           # Skriver ut sortedTree


 
