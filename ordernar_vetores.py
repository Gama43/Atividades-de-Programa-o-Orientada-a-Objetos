class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        self.array_para_ordenar = array_para_ordenar
        
    def ordena(self):
        self.ordena = self.array_para_ordenar
        for n in range(len(self.ordena)-1,0,-1):
          for i in range(n):
            if self.ordena[i]>self.ordena[i+1]:
                temp = self.ordena[i]
                self.ordena[i] = self.ordena[i+1]
                self.ordena[i+1] = temp
        return self.ordena

    def toString(self):
        self.toString = ','.join(str(e) for e in self.ordena)
        print(self.toString)
        return self.toString