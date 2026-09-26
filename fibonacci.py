import pandas as pd


MATRIZ_FIBONACCI = pd.DataFrame([
    [0, 1],
    [1, 1]
])

def fibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma lineal.

    Complejidad esperada:
        Tiempo: O(n)
        Espacio: O(1)

    Ejemplos:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(10) -> 55
    """
    if n == 0:
        return 0
    matriz = MATRIZ_FIBONACCI
    for _ in range(n - 1):
        matriz = matriz @ matriz
    return matriz.iloc[0, 1]


def probar(nombre, obtenido, esperado):
    assert obtenido == esperado, (
        f"{nombre} falló\n"
        f"Esperado: {esperado}\n"
        f"Obtenido: {obtenido}"
    )
    print(f"[OK] {nombre}: {obtenido}")


if __name__ == "__main__":
    probar("Fibonacci n=0", fibonacci(0), 0)
    probar("Fibonacci n=1", fibonacci(1), 1)
    probar("Fibonacci n=10", fibonacci(10), 55)

    print("\nTodas las pruebas de fibonacci.py pasaron.")
