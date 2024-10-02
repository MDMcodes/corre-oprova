#Uma empresa deseja gerenciar os salários de seus funcionários. Crie uma função que receba um dicionário com nomes de funcionários como chaves e seus salários como valores. Usando filter() e lambda, selecione apenas os funcionários que têm salários acima de um determinado valor. Depois, use map() para aplicar um aumento de 10% aos salários filtrados e retorne o dicionário atualizado.
#Dica: Você pode usar um loop for para reconstruir o dicionário após usar filter() e map().


func = {}

while True:
    #itens é o nome e values é o salario
    nome = input('digite o nome do funcionário: ')
    salario = int(input('digite o salário do funcinário: '))
    func.update({nome:salario})
    op = input('deseja cadastrar mais?  (s/n)').lower()
    if op == 'n':
        break

valordet = float(input('Digite o valor do salário mínimo: '))

print(func.items())
filtro = dict(filter(lambda x: x[1] > valordet, func.items()))
print("funcionários com salários maiores que o salário mínimo")
print(filtro) 


aumento = dict(map(lambda x: (x[0], x[1] * 1.15), filtro.items()))
print(aumento)

soma = sum(func.values())
media = (soma / len(func))
print(media)