#QUESTÃO 9

print("Qual o seu salario mensal atual?")
salario_atual = float(input())

print("Quanto foi o percentual de reajuste?")
percentual_reajuste = float(input())

reajuste = (percentual_reajuste / 100) * salario_atual

salario_reajustado = salario_atual + reajuste

print("Salario reajustado: R$" + str(salario_reajustado))
