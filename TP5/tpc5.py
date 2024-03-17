import re
import json

class Vending:
    def __init__(self, produtos_f="lista_produtos.json"):
        self.produtos = self.carrega(produtos_f)
        self.master = False
        self.saldo = 0

    def carrega(self, produtos_f):
        produtos = {}
        try:
            with open(produtos_f, 'r') as f:
                lista_produtos = json.load(f)
                for produto in lista_produtos:
                    codigo = produto['cod']
                    nome = produto['nome']
                    preco = int(produto['preco'] * 100)
                    quantidade = produto['quant']
                    produtos[codigo] = {'nome': nome.strip(), 'preco': preco, 'quant': quantidade}
        except FileNotFoundError:
            print(f"Erro: O arquivo {produtos_f} não foi encontrado.")
        return produtos

    def listar(self):
        print("cod    |  nome              |  quantidade  |  preço")
        print("---------------------------------------------------")
        for codigo, produto in self.produtos.items():
            p_euros = produto['preco'] // 100
            p_centimos = produto['preco'] % 100
            preco_formatado = f"{p_euros}e{p_centimos:02d}c"
            print(f"< {codigo:<7} {produto['nome']:<20} {produto['quant']:<13} {preco_formatado}")

    def moedas(self, moedas):
        for moeda in moedas:
            m = re.match(r'(\d+)([EC])', moeda)
            if m:
                valor, unidade = m.groups()
                if unidade == 'E':
                    if(re.match(r'^[12]$', valor)):
                        self.saldo += int(valor) * 100
                    else:
                        print(f"Moeda inválida: {moeda}")
                elif unidade == 'C':
                    if(re.match(r'^[125][0]?$', valor)):
                        self.saldo += int(valor)
                    else:
                        print(f"Moeda inválida: {moeda}")

            else:
                print(f"Moeda inválida: {moeda}")

        print(f"RESPOSTA < SALDO = {self.saldo//100}e{self.saldo%100}c")

    def comprar(self, produto_codigo):
        produto = self.produtos.get(produto_codigo)
        if produto:
            if produto['quant']>0:
                if self.saldo >= produto['preco']:
                    self.saldo -= produto['preco']
                    produto['quant'] -= 1
                    print(f"< Pode retirar o produto dispensado {produto['nome']}")
                    print(f"< SALDO {self.saldo//100}e{self.saldo%100}c")
                else:
                    print("Saldo insuficiente.")
            else:
                print(f"Já não existe stock do produto selecionado {produto['nome']}")
        else:
            print("Produto não encontrado.")

    def troco(self):
        moedas = []
        moedas.append((self.saldo // 200, "2e"))
        moedas.append(((self.saldo % 200) // 100, "1e"))
        moedas.append(((self.saldo % 100) // 50, "50c"))
        moedas.append(((self.saldo % 50) // 20, "20c"))
        moedas.append(((self.saldo % 50 % 20) // 10, "10c"))
        moedas.append(((self.saldo % 50 % 20 % 10) // 5, "5c"))
        moedas.append(((self.saldo % 50 % 20 % 10 % 5) // 2, "2c"))
        moedas.append(((self.saldo % 50 % 20 % 10 % 5 % 2), "1c"))

        moedas_formatadas = [f"{quantidade}x {valor}" for quantidade, valor in moedas if quantidade > 0]
        if moedas_formatadas:
            print("Pode retirar o troco:", ", ".join(moedas_formatadas))
        else:
            print("Não há troco disponível.")
        self.saldo = 0
    
    def add(self):
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        precod = float(input("Preço do produto (em euros): "))
        quantidade = int(input("Quantidade inicial do produto: "))

        preco = int(precod * 100)
        self.produtos[codigo] = {'nome': nome, 'preco': preco, 'quant': quantidade}
        print("Novo produto adicionado com sucesso!")
    
    def restock(self, produto_codigo):
        produto = self.produtos.get(produto_codigo)
        if produto:
            nquantidade = int(input("Unidades adicionadas: "))
            produto['quant'] += nquantidade
            print(f"Restock do produto feito com sucesso! Agora existe(m) {produto['quant']} unidade(s).")
        else:
            print("Produto não encontrado.")
        
    def update(self, produto_codigo):
        produto = self.produtos.get(produto_codigo)
        if produto:
            precod = float(input("Insira o novo preço do produto(em euros): "))
            preco = int(precod * 100)
            produto['preco'] = preco
            p_euros = produto['preco'] // 100
            p_centimos = produto['preco'] % 100
            preco_formatado = f"{p_euros}e{p_centimos:02d}c"
            print(f"Preço do produto atualizado com sucesso para {preco_formatado}")
        else:
            print("Produto não encontrado.")
    
    def remove(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")
    
    def m(self):
        while True:
            user_input = input("INPUT >> ").upper()
            content = user_input.split()
            
            add_m = re.match(r'ADD', content[0])
            listar_m = re.match(r'LISTAR', content[0])
            restock_m = re.match(r'RESTOCK', content[0])
            update_m = re.match(r'UPDATE', content[0])
            remove_m = re.match(r'REMOVE', content[0])
            sair_m = re.match(r'SAIR', content[0])

            if add_m:
                vending.add()
            elif listar_m:
                vending.listar()
            elif restock_m:
                vending.restock(content[1])
            elif update_m:
                vending.update(content[1])
            elif remove_m:
                vending.remove(content[1])
            elif sair_m:
                break
            else:
                print("Comando inválido.")


if __name__ == "__main__":
    vending = Vending()

    while True:
        user_input = input("INPUT >> ").upper()
        content = user_input.split()
        
        listar_m = re.match(r'LISTAR', content[0])
        master_m = re.match(r'2003', content[0])
        moedas_m = re.match(r'MOEDA', content[0])
        selecionar_m = re.match(r'SELECIONAR', content[0])
        sair_m = re.match(r'SAIR', content[0])

        if listar_m:
            vending.listar()
        elif master_m:
            print("Bem-vindo ao modo Master.")
            vending.m()
        elif moedas_m:
            vending.moedas(content[1:])
        elif selecionar_m:
            vending.comprar(content[1])
        elif sair_m:
            vending.troco()
            break
        else:
            print("Comando inválido.")
