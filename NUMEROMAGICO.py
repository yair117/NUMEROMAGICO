secret_number = 777


print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero=int(input("Ingresa el numero secreto\n"))

while secret_number!=numero:
    if (secret_number==numero):
        print()
    else:
        numero!=secret_number
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero=int(input("Ingresa el numero secreto\n"))

print("\t¡¡Ja, ja! ¡Felicidades, tuviste suerte muggle! Eres libre ahora.")