from termcolor import colored
from colorama import Fore
class RubiksCube:
    def __init__(self, size:int, *args, **kwargs) -> None:
        self.setSize(size)
        self.numPlaces = self.size **2 * 6 # size squared times 6 faces.
        pos = kwargs.get('pos', None)
        self.setPosition(pos)
        self.defineOperations()
        self.defineColors()
        
    def setSize(self, size):
        self.size = size
        self.calculatePosCorners()
        self.calculatePosEdges()
        self.calculatePosCenters()
    def setPosition(self, pos):
        if pos != None:
            self.position = pos
        else:
            self.position = list(range(self. numPlaces))
        
        if not self.validPos():
            raise Exception("Posición inválida")
    def solved(self):
        return  self.position == list(range(self. numPlaces))
    def validPos(self) -> bool:
        """Function that checks if a position is valid. A valid position needs to have the corners as corners, edges as edges, and centers as centers.
        """
        if self.checkCorners() and self.checkEdges() and self.checkCenters():
             return True
        else:
            return False
    def defineColors(self):
        self.colors = {"U":'yellow', "F":'green', "L":'red', "R":"magenta", "B":'blue', "D":'white'}
    def faceOfI(self, i):
        """"Function that determines the face this element belongs to, when the cube is solved"""
        s = self.size 
        if i >= 0 and i < s**2:
            return "U"
        elif i < 2 * s**2:
            return "F"
        elif i < 3 * s**2:
            return "D"
        elif i < 4 * s**2:
            return "L"
        elif i < 5 * s**2:
            return "R"
        elif i < 6 * s**2:
            return "B"
        else:
            raise Exception("Posición inválida, no pertenece a ninguna cara originalmente.")
    
    def getCurrentFace(self, face):
        """Function that returns a list of numbers that correspond to the selected face"""
        values = []
        for i in range(self.numPlaces):
            if self.faceOfI(i) == face:
                values.append(self.position[i])
        return values
    
    def printRow(self, faceName, nRow):
        """Function that recieves the name of a face and prints the row selected, nRow goes from 0 to size-1"""
        face = self.getCurrentFace(faceName)
        values = face[nRow * self.size: nRow * self.size + 3]
        for val in values:
            valString = f"{val:<3.0f}"
            color = self.colors[self.faceOfI(val)]
            print(colored(valString, color), end="") 
    def printEmptyRow(self):
        print("   " *self.size, end="")
        
    def printCube(self):
        
        emptyRow = "   " * 3
        #U
        for i in range(self.size):
            self.printEmptyRow()
            self.printRow("U", i)
            print("")
        # L, F, R, B
        for i in range(self.size):
            self.printRow("L", i)
            self.printRow("F", i)
            self.printRow("R", i)
            self.printRow("B", i)
            print("")
            
        #D
        for i in range(self.size):
            self.printEmptyRow()
            self.printRow("D", i)
            print("")
            
             
        
    def perm(self, i, j):
        """Function that performs a the permutation of two positions"""
        if i < self.numPlaces and j < self.numPlaces:
            valI = self.position[i]
            self.position[i] = self.position[j]
            self.position[j] = valI
        else:
            raise Exception("Ubicaciones para hacer las permutaciones inválidas.")
    def performOperation(self, operation):
        """Function that performs an operation. It receives the name of the operation"""
        newPosition = self.position.copy()
        for move in self.operations[operation]:
            newPosition[move[1]] = self.position[move[0]]
        self.position = newPosition
    def performOperations(self, opsString):
        """Function that recieves a string of operations and performs it"""
        ops = []
        for i in range(len(opsString)):
            if opsString[i] != "p":
                ops.append(opsString[i])
            else:
                ops[-1] += "p"
        for op in ops:
            print(op)
            self.performOperation(op)
    def defineOperations(self):
        """Each operation is composed of several tuples with two elements. The first position represents the element to be moved and the second one is the destination. All movements happen at the same time"""
        if self.size == 3:
            self.operations = {}
            #U
            self.operations["U"] = ((6, 0), (3, 1), (0, 2), (7, 3), (4, 4), (1, 5), (8, 6), (5, 7), (2, 8),(36,9),(37,10),(38,11),(9,27),(10,28),(11,29),(27,45),(28,46),(29,47),(45,36),(46,37),(47,38))
            self.operations["Up"] = tuple([(elem[1], elem[0]) for elem in self.operations["U"]])
            
            #D 
            self.operations["D"] = ((18,20),(19,23),(20,26),(21,19),(22,22),(23,25),(24,18),(25,24),(26,24), (51,33),(52,34),(53,35),(33,15),(34,16),(35,17),(15,42),(16,43),(17,44),(42,51),(43,52),(44,53),)
            self.operations["Dp"] = tuple([(elem[1], elem[0]) for elem in self.operations["D"]])
            
            #R
            self.operations["R"] = ((36,38),(37,41),(38,44),(41,43),(44,42),(43,39),(42,36),(39,37),(36,38), (11, 2), (14, 5), (17, 8), (2,51),(5,48),(8,45),(51,20),(48,23),(45,26),(20,11),(23,14),(26,17))
            self.operations["Rp"] = tuple([(elem[1], elem[0]) for elem in self.operations["R"]])
            
            #L
            self.operations["L"] =  ((27,29),(28,32),(29,35),(30,28),(31,31),(32,34),(33,27),(34,30),(35,33),(0,9),(3,12),(6,15),(9,18),(12,21),(15,24),(18,53),(21,50),(24,47),(53,0),(50,3),(47,6))
            self.operations["Lp"] = tuple([(elem[1], elem[0]) for elem in self.operations["L"]])
            
            #F
            self.operations["F"] = ((9,15),(10,12),(11,9),(12,16),(13,13),(14,10),(15,17),(16,14),(17,11),(6,36),(7,39),(8,42),(36,20),(39,19),(42,18),(20,35),(19,32),(18,29),(35,6),(32,7),(29,8))
            self.operations["Fp"] = tuple([(elem[1], elem[0]) for elem in self.operations["F"]])
            
            #B
            self.operations["B"] = ((45,47),(46,50),(47,53),(48,46),(49,49),(50,52),(51,45),(52,48),(53,51),(44,2),(41,1),(38,0),(2,27),(1,30),(0,33),(27,24),(30,25),(33,26),(24,44),(25,41),(26,38))
            self.operations["Bp"] = tuple([(elem[1], elem[0]) for elem in self.operations["B"]])
            
            
        else:
            raise Exception("Not implemented for cubes that are not 3x3")
    
    def getCenters(self):
        centers = ()
        for pos in self.posCenters:
            centers = (*centers, self.position[pos])
        return centers
    def getCorners(self):
        corners = []
        for pos in self.posCorners:
            corners.append((self.position[pos[0]], self.position[pos[1]], self.position[pos[2]]))
        return corners
    def getEdges(self):
        edges = []
        for pos in self.posEdges:
            edges.append((self.position[pos[0]], self.position[pos[1]]))
        return edges
    def checkCenters(self):
        if self.size == 3:
            centers = self.getCenters()
            # print(f"Current centers: {centers}")
            # print(f"Son iguales: {centers == self.posCenters}")
            return centers == self.posCenters
        else:
            raise Exception("Funcionalidad no implementada para cubos diferentes a 3x3")
    def checkCorners(self):
        sortedCurrentCorners = self.getCorners()
        sortedCurrentCorners = {tuple(sorted(elem)) for elem in sortedCurrentCorners}
        # print(f"Sorted current corners: {sortedCurrentCorners}")
        # print(f"Son iguales: {sortedCurrentCorners == self.posCorners}")
        return sortedCurrentCorners == self.posCorners

    def checkEdges(self):
        sortedCurrentEdges = self.getEdges()
        sortedCurrentEdges = {tuple(sorted(elem)) for elem in sortedCurrentEdges}
        # print(f"Sorted current edges: {sortedCurrentEdges}")
        # print(f"Son iguales: {sortedCurrentEdges == self.posEdges}")
        return sortedCurrentEdges == self.posEdges
                 
    def calculatePosEdges(self):
        if self.size == 3:
            e1 = (1, 46)
            e2 = (3, 28)
            e3 = (5, 37)
            e4 = (7, 10)
            e5 = (16,19 )
            e6 = (21, 34)
            e7 = (23,43 )
            e8 = (25,52 )
            e9 = (50,30 )
            e10 = (32,12 )
            e11 = (14,39 )
            e12 = (41,48 )
            self.posEdges = {e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12}
            self.posEdges = {tuple(sorted(elem)) for elem in self.posEdges}
            
        else:
            self.posEdges = None      
    def calculatePosCenters(self):
        if self.size == 3:
            self.posCenters = (4, 13, 22, 31, 40, 49)
        else:
            self.posCenters = None
        
    def calculatePosCorners(self):
        s = self.size
        c1 = ((s-1)*s, s*s, 3*s*s + s - 1)
        c2 = ((s-1)*s + s - 1, s*s + 2, 4*s*s)
        c3 = ((2*s-1)*s + s - 1, 2*s*s + s - 1, (5*s-1)*s)
        c4 = ((2*s-1)*s, 2*s*s, (4*s-1)*s + s - 1)
        c5 = (4*s*s + s - 1, 5*s*s, s - 1)
        c6 = ((5*s-1)*s + s - 1, (6*s- 1)*s, (3*s-1)*s + s - 1)
        c7 = (5*s*s + s - 1, 3*s*s, 0)
        c8 = ((4*s-1)*s, (6*s- 1)*s + s - 1, (3*s-1)*s)
        self.posCorners = {c1, c2, c3, c4, c5, c6, c7, c8}
        self.posCorners = {tuple(sorted(elem)) for elem in self.posCorners}
    def getPosCorners(self):
        return self.posCorners
    def getPosCenters(self):
        return self.posCenters
    def getPosEdges(self):
        return self.posEdges
    def getPosition(self):
        return self.position
    
if __name__ == "__main__":
    txt = RubiksCube(3)
    txt.printCube()
    txt.performOperations("RURpUpRURpUpRURpUpRURpUpRURpUpRURpUp")
    print(f"Solved: {txt.solved()}")
    txt.printCube()
    txt.performOperations("LUpLpULUpLpULUpLpULUpLpULUpLpULUpLpU")
    print(f"Solved: {txt.solved()}")
    txt.printCube()
    