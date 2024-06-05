numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

while True:
    print("soma, subtração, divisão, multiplicação")
    causa = input("qual operação você gostaria de realizar?: ")

    if causa == "soma":
        resultado = numero1 + numero2
    elif causa == "subtração":
        resultado = numero1 - numero2
    elif causa == "divisão":
        resultado = numero1 / numero2
    elif causa == "multiplicação":
        resultado = numero1 * numero2
    else:
        print("Operação inválida! Por favor, tente novamente.")
        continue

    print("O resultado da operação é:", resultado)

    n1 = input("Deseja trocar os números? (sim/não): ")
    if n1 == "não":
        break
    elif n1 == "sim":
        novo_numero1 = float(input("Qual o novo primeiro número? "))
        novo_numero2 = float(input("Qual o novo segundo número? "))

        numero1 = novo_numero1
        numero2 = novo_numero2
