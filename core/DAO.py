from model import Funcionario, Pessoa, Fornecedor, Estoque, Categoria, Produto, Venda


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(f'''{funcionario.id_funcionario}|{funcionario.clt}|{funcionario.nome}|{funcionario.cpf}|{funcionario.data_nascimento}|{funcionario.email}|{funcionario.endereco}''')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        func = []
        if len(cls.funcionarios) > 0:
            func = [Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6]) for i in cls.funcionarios]

        return func
    

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(f'{pessoa.nome}|{pessoa.cpf}|{pessoa.data_nascimento}|{pessoa.email}|{pessoa.endereco}')
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.pessoas = arq.readlines()
        
        cls.pessoas = list(map(lambda x: x.replace('\n', ''), cls.pessoas))
        cls.pessoas = list(map(lambda x: x.split('|'), cls.pessoas))

        pessoa = []
        if len(cls.pessoas) > 0:
            pessoa = [Pessoa(i[0], i[1], i[2], i[3], i[4]) for i in cls.pessoas]

        return pessoa
    

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(f'{fornecedor.nome}|{fornecedor.cnpj}|{fornecedor.telefone}|{fornecedor.categoria}')
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        if len(cls.fornecedor) > 0:
            forn = [Fornecedor(i[0], i[1], i[2], i[3]) for i in cls.fornecedor]

        return forn
    

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(f'{produto.nome}|{produto.preco}|{produto.categoria}|{str(quantidade)}')
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = [Estoque(Produto(i[0],i[1],i[2]), i[3]) for i in cls.estoque]

        return est


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        cat = [Categoria(i) for i in cls.categoria]

        return cat
    

class DaoVendas:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(f'{venda.itens_vendidos}|{venda.vendedor}|{venda.comprador}|{venda.quantidade_vendida}|{venda.data}')
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vendas = [Venda(i[0], i[1], i[2], i[3], i[4]) for i in cls.venda]

        return vendas