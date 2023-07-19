from datetime import datetime

class Pessoa:
    def __init__(self, nome, cpf, data_nascimento, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, id_funcionario, clt, nome, cpf, data_nascimento, email, endereco):
        self.id_funcionario = id_funcionario
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, data_nascimento, email, endereco)

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Venda:
    def __init__(self, itens_vendidos, vendedor, comprador, quantidade_vendida, data = datetime.now()):
        self.itens_vendidos = itens_vendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        self.data = data

