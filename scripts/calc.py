"""
Script de ejemplo para introducir argumentos de línea de comandos con argparse.

Este programa realiza una operación aritmética sencilla entre dos números
proporcionados por el usuario. Para esta primera versión, las operaciones
permitidas son:

- "sumar"  → suma de x y y
- "restar" → resta de x y y

Además, el usuario puede activar un modo "verbose" que imprime un mensaje más
informativo mostrando la operación completa. Si no se usa verbose, el programa
solo imprime el resultado numérico.

Ejemplos de uso:

    uv run scripts/calc.py 3 4
    uv run scripts/calc.py 10 7 --operacion restar
    uv run scripts/calc.py 5 6 --verbose

El objetivo principal de este script es mostrar cómo:
- definir argumentos obligatorios,
- definir opciones,
- y acceder a esos valores dentro del código.
"""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Realiza una operación aritmética simple entre dos números."
    )

    # Argumentos obligatorios: x y y
    parser.add_argument(
        "x",
        help="Primer número.",
        type=float,
    )
    parser.add_argument(
        "y",
        help="Segundo número.",
        type=float,
    )

    # Opción para elegir la operación
    parser.add_argument(
        "--operacion",
        choices=["sumar", "restar", "multiplicar", "dividir"],
        default="sumar",
        help="Operación aritmética básica a realizar: ('sumar' por defecto)",
    )

    # Opción para elegir la precisión
    parser.add_argument(
        "--precision",
        help="Número de cifras decimales.",
        type=int,
        default=4,
    )

    # Opción booleana "verbose"
    parser.add_argument(
        "--verbose",
        action="store_false",
        help="Si se activa, muestra una salida más detallada.",
    )

    args = parser.parse_args()

    # Lógica de la operación
    if args.operacion == "sumar":
        resultado = args.x + args.y
        operador = "+"
    elif args.operacion == "restar":
        resultado = args.x - args.y
        operador = "-"
    elif args.operacion == "multiplicar":
        resultado = args.x * args.y
        operador = "*"
    elif args.operacion == "dividir":
        resultado = args.x / args.y
        operador = "/"
    else:
        # Nunca debemos llegar aquí, pero en caso de que sí ...
        raise ValueError("Operación no permitida")

    # Redondear según la precisión pedida
    resultado = round(resultado, ndigits=args.precision)

    # Impresión según verbose
    if args.verbose:
        print(f"{resultado:.{args.precision}f}")
    else:
        print(f"{args.x} {operador} {args.y} = {resultado}")


if __name__ == "__main__":
    main()
