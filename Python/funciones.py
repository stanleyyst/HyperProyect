# def imprimir_mensaje():
#     print("mensaje especial")
#     print("Estoy aprendiendo funciones")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print("Hola")
    print("Bienvenido")
    print("Eligiste la option " + mensaje)

option = int(input("hola elige entre: 1, 2 y 3: "))

if option == 1:
    conversacion("1")
elif option == 2:
    conversacion("2")
elif option == 3:
    conversacion("3")
else:
    print("nonono ese no...")
