class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __str__(self):
        return str("\n".join(["\t".join([str(a) for a in i]) for i in matrx]))

    def __add__(self):
        matrx = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

        for i in range(len(self.list_1)):

            for a in range(len(self.list_2[i])):
                matrx[i][a] = self.list_1[i][a] + self.list_2[i][a]

        return str("\n".join(["\t".join([str(a) for a in i]) for i in matrx]))


my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[10, 11],
                    [12, 13, 14],
                    [15, 16, 17]])

print(my_matrix.__add__())
