import math

altura=float(input("digite a altura:   "))
coeficiente_arrasto=float(input("digite o coeficiente de arrasto:"))
massa = 1 
densidade_ar = 1.225 
area_secao_transversal = 0.1 
tempo_queda = math.sqrt((2 * massa) / (densidade_ar * area_secao_transversal * coeficiente_arrasto)) * math.acosh(math.exp(math.sqrt((densidade_ar * area_secao_transversal * coeficiente_arrasto) / (2 * massa)) * altura))

print(f"o tempo de queda é {tempo_queda}.")
