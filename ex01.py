receitas = []
despesas = []

while True:
    rec = float(input("Digite a receita mensal: "))
    desp = float(input("Digite a despesa mensal: "))
    receitas.append(rec)
    despesas.append(desp)
    opc = input("Adicionar mais?:  (s/n) ").lower()
    if opc == "n":
        break
    
#receitas = a, despesas = b
lucromensal = list(map(lambda a, b: a - b, receitas, despesas))

