import pandas as pd


MATRIZ_FIBONACCI = pd.DataFrame([
    [0, 1],
    [1, 1]
])


def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices 2x2 representadas como DataFrame.

    Puedes apoyarte en pandas para realizar la multiplicación matricial.
    """
    pass


def potencia_matriz(M, n):
    """
    Calcula M^n usando exponentiation by squaring.

    Complejidad esperada:
        Tiempo: O(log n)

    Debe regresar una matriz 2x2.
    """
    pass


def fibonacci_matricial(n):
    """
    Calcula el n-ésimo número de Fibonacci usando:

        [[0, 1],
         [1, 1]]^n

    donde:

        [[0, 1],      [[F(n-1), F(n)  ],
         [1, 1]]^n =  [F(n),   F(n+1)]]

    Complejidad esperada:
        Tiempo: O(log n)
    """
    pass


def probar(nombre, obtenido, esperado):
    assert obtenido == esperado, (
        f"{nombre} falló\n"
        f"Esperado: {esperado}\n"
        f"Obtenido: {obtenido}"
    )
    print(f"[OK] {nombre}: {obtenido}")


if __name__ == "__main__":
    probar("Fibonacci matricial n=0", fibonacci_matricial(0), 0)
    probar("Fibonacci matricial n=5", fibonacci_matricial(5), 5)
    probar("Fibonacci matricial n=10", fibonacci_matricial(10), 55)

    print("\nTodas las pruebas de fibonacci_matricial.py pasaron.")
