receitas = []
despesas = []
liq = []

while True:
    rec = float(input("Digite a receita mensal: "))
    desp = float(input("Digite a despesa mensal: "))
    receitas.append(rec)
    despesas.append(desp)
    #receitas = a, despesas = b
    lucromensal = list(map(lambda a, b: a - b, receitas, despesas))
    liq.append(lucromensal)
    print(sum(liq))
    anual = sum(liq) / len(liq) #sum = pegar todos os valores da lista e somar, len = contar quantos valores tem na lista
    print(f"O lucro mensal é: {lucromensal}")
