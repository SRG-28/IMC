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
    if 18.5 <= imc < 24.9:
        print("Peso normal")
    if 25 <= imc < 29.9:
        print("Sobrepeso")
    if 30 <= imc:
        print("Obesidad")
    op=input("¿Desea continuar usando nuestro sistema? (Si/No) ").upper()
print("Gracias por usar nuestro sistema")
