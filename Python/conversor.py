# colones = float(input("Ingresa los colones que tienes: "))
# valor_dolar = 611
# dolares = str(round(colones / valor_dolar, 2))
# print("Tienes $" + dolares + " dólares.")

# dolares = float(input("How many dollars do you have?: "))
# tipo_cambio = 611
# colones = str(round(dolares * tipo_cambio, 2))
# print("You currently have C" + colones + " colons in your bank")

menu = """"
Bienvenido al conversor de monedas.😍

1 Pesos Colombianos
2 Colones
3 Euros

Elige una moneda: """

option = int(input(menu))

if option == 1:
    pesos = int(input("Cuantos pesos tienes?: "))
    tipo_cambio = 3777.76
    dolares = str(round(pesos/ tipo_cambio,2))
    print("Tienes $" + dolares + " dolares actualmente.")

elif option == 2:
    colones = int(input("Cuantos colones tienes?: "))
    tipo_cambio = 611.77
    dolares = str(round(colones/ tipo_cambio,2))
    print("Tienes $" + dolares + " dolares actualmente.")

elif option == 3:
    euros = int(input("Cuantos euros tienes?: "))
    tipo_cambio = 0.82
    dolares = str(round(euros*tipo_cambio,2))
    print("Tienes $" + dolares + " dolares actualmente.")

else:
    print("Ingresa un valor correcto...")