class Produto:
    def __init__(self,nome, quantidade) :
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self,produto):
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade
    
    def verifica_quantidade(self,nome_produto):
        print(self.produtos.get(nome_produto, 0))
        return self.produtos.get(nome_produto, 0)