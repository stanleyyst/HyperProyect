# colones = float(input("Ingresa los colones que tienes: "))
# valor_dolar = 611
# dolares = str(round(colones / valor_dolar, 2))
# print("Tienes $" + dolares + " dólares.")

# dolares = float(input("How many dollars do you have?: "))
# tipo_cambio = 611
# colones = str(round(dolares * tipo_cambio, 2))
# print("You currently have C" + colones + " colons in your bank")

def conversor(moneda, cambio):
    capital = int(input("Cuantos " + moneda + " tienes?: "))
    tipo_cambio = cambio
    dolares = str(round(capital/ tipo_cambio,2))
    print("Tienes $" + dolares + " dolares actualmente.")

def dolar(divisa, cambio):
    capital = int(input("Cuantos dolares tienes?: "))
    tipo_cambio = cambio
    currency = str(round(capital * tipo_cambio,2))
    print("Tienes $" + currency + " " + divisa + " actualmente.")

menu = """
Bienvenido al conversor de monedas.

Tienes dolares o moneda local?:
1- Dolares
2- Moneda local

Elige tipo de conversion: """

option = int(input(menu))

if option == 1:
    menu = """
================================

1- Pesos Col.
2- Colones
3- Euros

A cual moneda quieres convertir?: """

    opcion = int(input(menu))
    
    if opcion == 1:
        dolar("pesos", 3724.63)

    elif opcion == 2:
        dolar("colones", 616.90)

    elif opcion == 3:
        dolar("euros", 0.83)

    else:
        print("Ingresa un valor correcto...")
    dolar
elif option == 2:
    menu = """
================================
1- Pesos Col.
2- Colones
3- Euros

Elige la divisas que tienes para convertir a USD: """

    option = int(input(menu))

    if option == 1:
        conversor("pesos", 616.90)

    elif option == 2:
        conversor("colones", 616.90)

    elif option == 3:
        conversor("euros", 0.83)

    else:
        print("Ingresa un valor correcto...")
else:
    print("Ingresa un valor valido..")