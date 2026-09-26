def exponenciacion_rapida(x, n):
    """
    Calcula x^n usando exponentiation by squaring.

    Complejidad esperada:
        Tiempo: O(log n)

    Ejemplos:
        exponenciacion_rapida(2, 0) -> 1
        exponenciacion_rapida(2, 10) -> 1024
        exponenciacion_rapida(5, 3) -> 125
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
    probar("2^0", exponenciacion_rapida(2, 0), 1)
    probar("2^10", exponenciacion_rapida(2, 10), 1024)
    probar("5^3", exponenciacion_rapida(5, 3), 125)

    print("\nTodas las pruebas de exponenciacion_rapida.py pasaron.")
