# Pede um numero ao usuario
numero = int(input("Digite um numero entre 1 e 20: "))

# Condição e validade usando operador logico
if numero <= 20 and numero >= 1:
    if numero < 10:
        print("O numero é menor que 10!")

    elif numero > 18:
        print("O numero é maior que 18.")

    elif numero == 17:
        print("O numero é igual a 17.")

    else:
        print("O numero é >= que 10, diferente de 17 e <= que 18.")

else:
    print("Numero invalido!")    