  # УРОК_Функции в Python. Функция с параметром
def get_matrix(n, m, value):   # Пишем функцию get_matrix и пишем в ней параметры n, m и value
    matrix = []      # Пустой список matrix внутри функции get_matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value) # в каждый внутренний список добавляется m value
    return matrix  # возвращение результата

matrix_1 = get_matrix(2, 2, 10)
matrix_2 = get_matrix(3, 5, 42)
matrix_3 = get_matrix(4, 2, 13)
print(matrix_1)
print(matrix_2)
print(matrix_3)