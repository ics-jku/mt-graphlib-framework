paths = []


def house(matrix, start, kn, count, path):
    for i in range(0, 5):
        if matrix[kn][i] == 1:
            new_path = []
            new_path.extend(path)
            new_path.append(i)
            if count == 7:
                if start == 0:
                    paths.append(new_path)
                return
            matrix[kn][i] = 0
            matrix[i][kn] = 0
            house(matrix, start, i, count+1, new_path)
            matrix[kn][i] = 1
            matrix[i][kn] = 1


def calculate():
    matrix = [[0, 1, 1, 1, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 0, 1],
              [0, 0, 1, 1, 0]]
    house(matrix, 0, 0, 0, [0])


calculate()
