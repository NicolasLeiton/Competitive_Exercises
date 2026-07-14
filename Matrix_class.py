class matrix():
    def __init__(self, values:list):
        self.values = values
        self.rows = len(values)
        self.columns = len(values[0])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Las columnas no son del mismo tamaño")
        
        salida = [[0 for _ in range(self.columns)]
          for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                salida[i][j] = self.values[i][j] + other.values[i][j]

        return matrix(salida)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")

        salida = [[0 for _ in range(other.columns)]
                for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    salida[i][j] += self.values[i][k] * other.values[k][j]

        return matrix(salida)
    
    
    def __pow__(self, exponent):
        if self.rows != self.columns:
            raise ValueError("Solo las matrices cuadradas pueden elevarse a una potencia.")

        result = matrix([[1 if i == j else 0 for j in range(self.rows)]
                   for i in range(self.rows)])
        base = self

        while exponent > 0:
            if exponent % 2 == 1:
                result = result * base

            base = base * base
            exponent //= 2

        return result
    
    def __str__(self):
        return "\n".join(" ".join(map(str, fila)) for fila in self.values)
    
    def __eq__(self, other):
        return self.values == other.values
    

A = matrix([
    [1, 2],
    [3, 4]
])

B = matrix([
    [5, 6],
    [7, 8]
])

print(A*B)