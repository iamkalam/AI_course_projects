import random
import math


class MiniNumPy:

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

#creation funcitons 

    @staticmethod
    def fromlisst(lst):
        return MiniNumPy(lst)

    @staticmethod
    def zeros(r, c):
        return MiniNumPy([[0 for _ in range(c)] for _ in range(r)])

    @staticmethod
    def ones(r, c):
        return MiniNumPy([[1 for _ in range(c)] for _ in range(r)])

    @staticmethod
    def random(r, c):
        return MiniNumPy([[random.random() for _ in range(c)] for _ in range(r)])

#shape 

    def shape(self):
        return (self.rows, self.cols)

#reshape

    def reshape(self, r, c):

        flat = [item for row in self.data for item in row]

        if len(flat) != r * c:
            raise ValueError("Invalid_reshape")

        new = []
        index = 0

        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[index])
                index += 1
            new.append(row)

        return MiniNumPy(new)
#elemet operations

    def __add__(self, other):

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return MiniNumPy(result)

    def __sub__(self, other):

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return MiniNumPy(result)

    def __mul__(self, other):

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * other.data[i][j])
            result.append(row)

        return MiniNumPy(result)
#muktiplication (dot product)   

    def __matmul__(self, other):

        if self.cols != other.rows:
            raise ValueError("matrix dimensions do not match")

        result = []

        for i in range(self.rows):
            row = []

            for j in range(other.cols):

                s = 0

                for k in range(self.cols):
                    s += self.data[i][k] * other.data[k][j]

                row.append(s)

            result.append(row)

        return MiniNumPy(result)

#transpose
    def transpose(self):

        result = []

        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            result.append(row)

        return MiniNumPy(result)

    # ------------------------
    # SUM
    # ------------------------

    def sum(self, axis=None):

        if axis is None:
            return sum(sum(row) for row in self.data)

        if axis == 0:
            return [sum(self.data[i][j] for i in range(self.rows)) for j in range(self.cols)]

        if axis == 1:
            return [sum(row) for row in self.data]

#mean 

    def mean(self):

        total = self.sum()
        count = self.rows * self.cols

        return total / count
#standard deviation

    def std(self):

        m = self.mean()

        total = 0

        for row in self.data:
            for val in row:
                total += (val - m) ** 2

        return math.sqrt(total / (self.rows * self.cols))


#boolenan operations

    def greater_than(self, threshold):

        result = []

        for row in self.data:
            r = []
            for val in row:
                r.append(val > threshold)
            result.append(r)

        return result

#indexing 

    def __getitem__(self, index):
        return self.data[index]

#print 
    def __str__(self):

        output = ""

        for row in self.data:
            output += " ".join(f"{x:8.3f}" for x in row) + "\n"

        return output




# Input layer (1 sample, 3 features)
X = MiniNumPy.fromlisst([[1, 2, 3]])

# Weights (3 inputs -> 2 neurons)
W = MiniNumPy.fromlisst([
    [0.2, 0.5],
    [0.3, 0.7],
    [0.6, 0.1]
])

# Bias
B = MiniNumPy.fromlisst([[0.1, 0.1]])

# Forward pass
Z = (X @ W) + B

print("Input:")
print(X)

print("weights:")
print(W)

print("output of Neural Layer:")
print(Z)