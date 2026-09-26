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
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == 2:
        return x * x

    #Caso Par
    if n % 2 == 0:
        return exponenciacion_rapida(exponenciacion_rapida(x,2), n//2)
    #Caso Impar
    else:
        return x * exponenciacion_rapida(exponenciacion_rapida(x,2), (n-1)//2)


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
