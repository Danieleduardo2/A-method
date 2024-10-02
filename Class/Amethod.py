import heapq
 
class Mapas:
    def __init__(self):
        self.MapaDeCiudades = [
            [10, 0,  0, "A"],    # Nodo A
            [8,  4,  1, "B"],    # Nodo B
            [7,  6,  2, "C"],    # Nodo C
            [6,  8,  3, "D"],    # Nodo D
            [6,  3,  4, "E"],    # Nodo E
            [5,  5,  5, "F"],    # Nodo F
            [3,  9,  6, "G"],    # Nodo G
            [4,  2,  7, "H"],    # Nodo H
            [2,  7,  8, "I"],    # Nodo I
            [3,  6,  9, "J"],    # Nodo J
            [1, 10, 10, "K"],    # Nodo K
            [0, 12, 11, "L"],    # Nodo L (objetivo)
            [9, 11, 12, "M"],    # Nodo M
            [5, 13, 13, "N"],    # Nodo N
        ]
        self.MapaDeCiudadesA = [
            [10, 0,  10, 0, "A"],    # Nodo A (0 + 10)
            [12, 1,  8, 4, "B"],     # Nodo B (1 + 8)
            [13, 2,  7, 6, "C"],     # Nodo C (7 + 6)
            [14, 3,  6, 8, "D"],     # Nodo D (6 + 8)
            [9,  4,  6, 3, "E"],     # Nodo E (6 + 3)
            [10, 5,  5, 5, "F"],     # Nodo F (5 + 5)
            [12, 6,  3, 9, "G"],     # Nodo G (3 + 9)
            [6,  7,  4, 2, "H"],     # Nodo H (4 + 2)
            [9,  8,  2, 7, "I"],     # Nodo I (2 + 7)
            [9,  9,  3, 6, "J"],     # Nodo J (3 + 6)
            [11, 10, 1, 10, "K"],    # Nodo K (1 + 10)
            [12, 11, 0, 12, "L"],    # Nodo L (0 + 12) (objetivo)
            [20, 12, 9, 11, "M"],     # Nodo M (9 + 11)
            [18, 13, 5, 13, "N"],     # Nodo N (5 + 13)
        ]
        self.matriz_adyacencia = [
            # A  B  C  D  E  F  G  H  I  J  K  L  M  N
            [ 0, 4, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
            [ 4, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
            [ 0, 2, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # C
            [ 0, 5, 3, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0],  # D
            [ 3, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0],  # E
            [ 0, 0, 1, 4, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0],  # F
            [ 0, 0, 0, 6, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0],  # G
            [ 0, 0, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0, 0, 0],  # H
            [ 0, 0, 0, 0, 0, 2, 3, 0, 0, 4, 1, 0, 0, 0],  # I
            [ 0, 0, 0, 0, 0, 0, 2, 5, 4, 0, 3, 0, 0, 0],  # J
            [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 2, 0, 0],  # K
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 5, 4],  # L
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 3],  # M
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0],  # N
        ]
        self.ListaV = []
        self.ColaPrioridad = [[10, 0, 0, "A"]]
        self.Actual=[]

    def getNeighbor(self):
        if len(self.ColaPrioridad) == 0 :
           print("Error la cola esta vacia y no se ha hallado el elemento")
        else:
            self.Actual=heapq.heappop(self.ColaPrioridad)
            if self.Actual[3]=="L":
               self.ListaV.append(self.Actual)
               return self.ListaV
            
            print("Actual: " + str(self.Actual)) 
            print("Cola de prioridad:"+ str(self.ColaPrioridad))  
            print("Lista de visitados"+ str(self.ListaV))
            print("")        
            for i in range(len(self.matriz_adyacencia)):
                if self.matriz_adyacencia[self.Actual[2]][i] != 0:
                   if self.isVisited(self.getCity(i)) == False: 
                      heapq.heappush(self.ColaPrioridad, self.getCity(i))
            self.ListaV.append(self.Actual)
            self.getNeighbor()       
    
    def isVisited(self, element):
        for i in range(len(self.ListaV)):
            if self.ListaV[i][2] == element[2]:
                print(element[2])
                return True
        return False
    
    def getCity(self, indice):
        for i in range(len(self.MapaDeCiudades)):
            if self.MapaDeCiudades[i][2] == indice:
               return self.MapaDeCiudades[i] 
    def recovery(self):
        self.ListaV.clear
        self.Actual.clear

Prueba = Mapas()
Prueba.getNeighbor()
print(Prueba.ListaV)
   