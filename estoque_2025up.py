produtos = {}

def cadastrar():
    nome = input("Produto: ").strip()
    if nome in produtos:
        print("Já existe.")
        return
    try:
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
    except:
        print("Valor inválido.")
        return
    produtos[nome] = {"preco": preco, "estoque": estoque}
    print("Cadastrado!")

def pedir():
    if not produtos:
        print("Nenhum produto.")
        return
    pedido = {}
    while True:
        print("Produtos:")
        for p, i in produtos.items():
            print(f"{p} - R${i['preco']} (Estoque: {i['estoque']})")
        p = input("Produto (fim p/ sair): ").strip()
        if p.lower() == "fim":
            break
        if p not in produtos:
            print("Não existe.")
            continue
        try:
            q = int(input("Qtd: "))
        except:
            print("Qtd inválida.")
            continue
        if q > produtos[p]["estoque"]:
            print("Sem estoque.")
            continue
        pedido[p] = pedido.get(p, 0) + q
        produtos[p]["estoque"] -= q
        print("Adicionado.")
    if pedido:
        total = sum(produtos[p]["preco"] * q for p, q in pedido.items())
        print("Resumo:")
        for p, q in pedido.items():
            print(f"{p}: {q} x R${produtos[p]['preco']} = R${produtos[p]['preco']*q}")
        print(f"Total: R${total}")

def menu():
    while True:
        op = input("1-Cadastrar 2-Pedir 0-Sair: ")
        if op == "1":
            cadastrar()
        elif op == "2":
            pedir()
        elif op == "0":
            break
        else:
            print("Inválido.")

if __name__ == "__main__":
    menu()