receitas = []
despesas = []
listaMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
lucroliq = []

for i in range(2):
    rec = float(input(f"Digite a receita do mês: "))
    desp = float(input(f"Digite a despesa do mês: "))
    receitas.append(rec)
    despesas.append(desp)


#receitas = a, despesas = b
lucromensal = list(map(lambda a, b: a - b, receitas, despesas))
lucroliq.append(lucromensal)
print(lucroliq)
soma = sum(lucromensal) #sum = soma de tudo q esta dentro da lista
media_anual = (soma / len(lucromensal)) #len = pega a quantidade de elementos dentro da lista
print(media_anual)

#pesquisei pra fazer esse for, n entendi direito
prejuizos = list(filter(lambda x: x < 0, lucromensal))
for i, valor in enumerate(prejuizos):  #enumerate = pega a posição e o valor
    print(f'O prejuízo foi: {valor} no mês de: {listaMeses[lucromensal.index(valor)]}')
