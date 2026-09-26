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
    pass


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
