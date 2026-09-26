import pandas as pd


MATRIZ_FIBONACCI = pd.DataFrame([
    [0, 1],
    [1, 1]
])


def potencia_matriz(M, n):
    """
    Calcula M^n usando exponentiation by squaring.

    Complejidad esperada:
        Tiempo: O(log n)

    Debe regresar una matriz 2x2.
    """
    #Casos Base
    if n == 0:
        return pd.DataFrame([
            [1, 0],
            [0, 1]
        ])

    if n == 1:
        return M

    if n == 2:
        return M @ M

    #Caso Par
    if n % 2 == 0:
        return potencia_matriz(potencia_matriz(M,2), n//2)
    #Caso Impar
    else:
        return M @ potencia_matriz(potencia_matriz(M,2), (n-1)//2)


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
    matriz = potencia_matriz(MATRIZ_FIBONACCI, n)
    return matriz.iloc[0, 1]


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

