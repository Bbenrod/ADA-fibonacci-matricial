# Fibonacci y Exponenciación Rápida

Proyecto base para implementar tres algoritmos:

1. Fibonacci en tiempo lineal `O(n)`.
2. Exponenciación rápida (`exponentiation by squaring`) en `O(log n)`.
3. Fibonacci matricial usando exponenciación rápida en `O(log n)`.

## Estructura

```text
fibonacci-exponenciacion/
├── fibonacci.py
├── exponenciacion_rapida.py
├── fibonacci_matricial.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux / macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

Ejecuta cada algoritmo por separado:

```bash
python fibonacci.py
python exponenciacion_rapida.py
python fibonacci_matricial.py
```

Cada script incluye tres casos de prueba con `assert`.

Las funciones principales están vacías con `pass` para que implementes los algoritmos.
