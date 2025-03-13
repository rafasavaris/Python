# CALCULO DA ÁREA DE UM CIRCULO
import math as m

raio = int(input("Digite o raio do circulo: "))

area = m.pi * (raio ** 2)

#  impressão do valor da éa com arredondamento
print(f"O valor da área é: {area:.3f}")
