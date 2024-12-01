#Tercer Ejercicio
#Sofía Rubie García

op = ""
print("--- Índice de Masa Corporal ---")
while(op != "NO"):
    peso = float(input("Digite su peso en kilogramos: "))
    altura=float(input("Digite su altura en metro: "))
    imc = peso / (altura ** 2)
    print("IMC: ", imc)

    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else: #IMC >= 30
        print("Obesidad")
    op=input("¿Desea continuar usando nuestro sistema? (Si/No) ").upper()
print("Gracias por usar nuestro sistema")
