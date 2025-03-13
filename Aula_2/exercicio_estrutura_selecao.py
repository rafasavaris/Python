# Pede um numero ao usuário
numero = int(input("Digite um numero entre 1 e 20: "))

# Testa se o numero é menor ou igual a 20 (validade)
if numero <= 20:
    # Testa se o numero é maior ou igual a 1 (validade)
    if numero >= 1: # dica: olhem a indentação!!
        if numero < 10:
            print("O numero é menor que 10!")

        elif numero > 18:
            print("O numero é maior que 18.")

        elif numero == 17:
            print("O numero é igual a 17.")

        else:
            print("O numero é >= que 10, diferente de 17 e <= que 18.")
    else:
        print("Numero invalido! Numero menor que 1")
else:
    print("Numero invalido! Numero maior que 20")
    