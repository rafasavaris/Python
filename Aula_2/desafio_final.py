# DESAFIO FINAL: PEDIR 3 NOTAS AO USUÁRIO E CALCULAR A MÉDIA. SE A MÉDIA FOR MENOR QUE
# 3.5 É REPROVAÇÃO; ENTRE 3.5 E 5.5, RECUPERAÇÃO. MAIOR QUE 5.5 É APROVADO!

# Pede 3 notas ao usuario
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Calcula a media
media = (n1 + n2 + n3)/3

# Testa se a media é menor que 3.5
if media < 3.5:
    print(f"A média do aluno é {media:.2f}. Aluno reprovado :(")
# Elif media >= 3.5 and media < 5.5: - jeito 1 de testar
elif 3.5 <= media <= 5.5: # jeito 2 de testar
    print(f"A média do aluno é {media:.2f}. Aluno está em rec")
else:
    print(f"A média do aluno é {media:.2f}. Aluno aprovado!!!!")