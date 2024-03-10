import re

class Vending:
    def __init__(self, produtos_f="lista_produtos.txt"):
        self.produtoss = self.carrega(produtos_f)
        self.saldo = 0

    def carrega(self, produtos_f):
        produtoss = {}
        try:
            with open(produtos_f, 'r') as f:
                for linhas in f:
                    m = re.match(r'(\d+)\s+([\w\s]+)\s+-\s+(\d+)c', linhas)
                    if m:
                        codigo, nome, preco = m.groups()
                        produtoss[codigo] = {'nome': nome.strip(), 'preco': int(preco)}
        except FileNotFoundError:
            print(f"Erro: O arquivo {produtos_f} não foi encontrado.")
        return produtoss

    def listar(self):
        print("LISTAR")
        for codigo, produtos in self.produtoss.items():
            p_euros = produtos['preco'] // 100
            p_centimos = produtos['preco'] % 100
            print(f"< {codigo} {produtos['nome']} {p_euros}e{p_centimos}c")

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

    def produtos(self, produtos_codigo):
        produtos = self.produtoss.get(produtos_codigo)
        if produtos:
            if self.saldo >= produtos['preco']:
                self.saldo -= produtos['preco']
                print(f"< SALDO {self.saldo//100}e{self.saldo%100}c")
            else:
                print("Saldo insuficiente.")
        else:
            print("Produto não encontrado.")

    def troco(self):
        print(f"Troco: {self.saldo//100}e{self.saldo%100}c")
        self.saldo = 0

if __name__ == "__main__":
    vendingm = Vending()

    while True:
        user_input = input("INPUT >> ").upper()
        content = user_input.split()
        
        listar_m = re.match(r'LISTAR', content[0])
        moedas_m = re.match(r'MOEDA', content[0])
        selecionar_m = re.match(r'SELECIONAR', content[0])
        sair_m = re.match(r'SAIR', content[0])

        if listar_m:
            vendingm.listar()
        elif moedas_m:
            vendingm.moedas(content[1:])
        elif selecionar_m:
            vendingm.produtos(content[1])
        elif sair_m:
            vendingm.troco()
            break
        else:
            print("Comando inválido.")
