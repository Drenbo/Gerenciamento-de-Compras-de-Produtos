positivo = {"Sim", "sim", "S", "s"}
negativo = {"Não", "não", "Nao", "nao", "N", "n"}
produtos = []
valores = []

processo = True

def maior_mil(valores):
    superior = 0
    for i in valores:
        if i > 1000:
            superior += 1 
        else:
            continue
    return superior

def menor_valor(valores, produtos):
    menor = min(valores)
    indice = valores.index(menor)
    nome = produtos[indice]
    return(nome)

while processo:
    interacao = input("Deseja criar uma lista de compras? ")
    while interacao in positivo:
        produto = input("Qual o produto? ")
        produtos.append(produto)
        valor = input("Qual o valor? ")
        valores.append(int(valor))
        interacao = input("Deseja continuar? ")
    else:
        total = sum(valores)
        print(f"O valor total das compras foi: {total}")
        print(f"Há {maior_mil(valores)} produtos com valor superior de 1000")
        print(f"O produto com menor valor foi {menor_valor(valores, produtos)}")
