from scipy.sparse import csr_matrix

class SparseMatrixCSR:
    def __init__(self, matrix):
        self.matrix = matrix
        self.values = []
        self.col_indices = []
        self.row_ptr = [0]
        self._compress()

    def _compress(self):
        non_zero_count = 0
        for row in self.matrix:
            for col_idx, value in enumerate(row):
                if value != 0:
                    self.values.append(value)
                    self.col_indices.append(col_idx)
                    non_zero_count += 1
            self.row_ptr.append(non_zero_count)

    def to_dense(self):
        dense_matrix = []
        for row_num in range(len(self.row_ptr) - 1):
            row = [0] * len(self.matrix[0])
            start = self.row_ptr[row_num]
            end = self.row_ptr[row_num + 1]
            for idx in range(start, end):
                col_idx = self.col_indices[idx]
                row[col_idx] = self.values[idx]
            dense_matrix.append(row)
        return dense_matrix

def process_matrix(matrix):
    try:
        sparse_csr = SparseMatrixCSR(matrix)
        custom_dense = sparse_csr.to_dense()
        sparse_scipy = csr_matrix(matrix)
        scipy_dense = sparse_scipy.toarray()

        csr_result = f"Valores no nulos: {sparse_csr.values}\n"
        csr_result += f"Índices de columna: {sparse_csr.col_indices}\n"
        csr_result += f"Puntero de filas: {sparse_csr.row_ptr}\n"
        csr_result += f"Matriz densa reconstruida: {custom_dense}\n"

        scipy_result = "\nComparación con scipy:\n"
        scipy_result += f"Valores no nulos (scipy): {sparse_scipy.data.tolist()}\n"
        scipy_result += f"Índices de columna (scipy): {sparse_scipy.indices.tolist()}\n"
        scipy_result += f"Puntero de filas (scipy): {sparse_scipy.indptr.tolist()}\n"
        scipy_result += f"Matriz densa reconstruida (scipy): {scipy_dense}\n"

        print(csr_result + scipy_result)
    except Exception as e:
        print(f"Hubo un problema con la entrada: {e}")

def get_matrix_from_input():
    try:
        # Solicita el número de filas y columnas
        num_rows = int(input("Introduce el número de filas: "))
        num_cols = int(input("Introduce el número de columnas: "))

        # Solicita los datos de la matriz
        print(f"Introduce los datos de la matriz fila por fila (separados por espacios):")
        matrix = []
        for i in range(num_rows):
            row = list(map(int, input(f"Fila {i + 1}: ").split()))
            if len(row) != num_cols:
                raise ValueError(f"Cada fila debe tener {num_cols} columnas.")
            matrix.append(row)

        return matrix
    except Exception as e:
        print(f"Hubo un problema con la entrada: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    matrix = get_matrix_from_input()
    if matrix:
        process_matrix(matrix)
