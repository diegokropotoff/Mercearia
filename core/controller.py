from model import Funcionario, Pessoa, Fornecedor, Estoque, Categoria, Produto, Venda
from DAO import DaoCategoria, DaoPessoa, DaoEstoque, DaoFornecedor, DaoFuncionario, DaoVendas
from datetime import datetime


class ControllerCategoria:

    def cadastrar_categoria(self, novaCategoria):
        existe = False
        cat = DaoCategoria.ler()

        for i in cat:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria registrada com sucesso')

        else:
            print('Categoria já existente. Por favor digite outra categoria')


    def alterar_categoria(self, categoria, nova_categoria):
        cat = DaoCategoria.ler()
        existe = False

        for i in cat:
            if i.categoria == nova_categoria:
                existe = True
            else:
                if i.categoria == categoria:
                    i.categoria = nova_categoria
                    print('Categoria alterada com sucesso.')
        
        if not existe:
            with open('categorias.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in cat:
                DaoCategoria.salvar(i.categoria)
        else:
            print('Categoria já existente.')


    def remover_categoria(self, categoria):
        cat = DaoCategoria.ler()

        for i in cat:
            if i.categoria == categoria:
                cat.pop(cat.index(i))
        with open('categorias.txt', 'r+') as arq:
            arq.truncate(0)
            arq.seek(0)
        for i in cat:
            DaoCategoria.salvar(i.categoria)
        print('Categoria removida com sucesso')
    

    def imprimir_categorias(self):
        cat = DaoCategoria.ler()
        print('\n')
        for i, k in enumerate(cat):
            print(f'{i+1}-{k.categoria}')
        print('\n')


class ControllerEstoque:
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        est = DaoEstoque.ler()
        existe = False
        catexiste = False
        for i in DaoCategoria.ler():
            if i.categoria == categoria:
                catexiste = True
        if catexiste:
            produto = Produto(nome, preco, categoria)
            for i in est:
                if i.produto == produto:
                    existe = True

            if not existe:
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            
            else:
                decisao = input('Produto já existente, deseja acrescentar à quantidade existente?(S/N)')
                if decisao in 'Ss':
                    for i in est:
                        if i.produto == produto:
                            i.quantidade += quantidade
        else:
            print('Categoria inexistente.')


    def alterar_produto(self, nome, novo_nome, novo_preco, nova_categoria, quantidade):
        existe = False
        est = DaoEstoque.ler()

        novo_produto = Produto(novo_nome, novo_preco, nova_categoria)
        for i in est:
            if i.produto == novo_produto:
                existe = True
            else:
                if i.produto.nome == nome:
                    i.produto = novo_produto
                    i.quantidade = quantidade
            
        if not existe:
            with open('estoque.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            
            for i in est:
                DaoEstoque.salvar(i.produto, i.quantidade)
                ('Produto alterado com sucesso')
        else:
            print('Produto já existente.')


    def remover_produto(self, nome):
        est = DaoEstoque.ler()
        
        for i in est:
            if i.produto.nome == nome:
                est.pop(est.index(i))
                print('Produto removido com sucesso')
        with open('estoque.txt', 'r+') as arq:
            arq.truncate(0)
            arq.seek(0)
        for i in est:
            DaoEstoque.salvar(i.produto, i.quantidade)


    def atualizar_estoque(self, nome, quantidade, aumentar = True):
        est = DaoEstoque.ler()
        for i in est:
            if i.produto.nome == nome:
                if not aumentar:
                    i.quantidade = int(i.quantidade) - int(quantidade)
                else:
                    i.quantidade = int(i.quantidade) + int(quantidade)

        with open('estoque.txt', 'r+') as arq:
            arq.truncate(0)
            arq.seek(0)
            
        for i in est:
            DaoEstoque.salvar(i.produto, i.quantidade)
            
        


    def imprimir_estoque(self):
        est = DaoEstoque.ler()
        print('    Nome |  Preço  |  Categoria  |  Quantidade')
        print('-'*80)
        for i, k in enumerate(est):
            print(f'{i} - {k.produto.nome} | R${k.produto.preco} | {k.produto.categoria} | {k.quantidade}')


class ControllerPessoa:

    def valida_cpf(self, cpf):
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) != 11:
            return False
        else:
            c = 10
            soma = 0
            for i in cpf[0:9]:
                soma += int(i)*c
                c -= 1
            soma *= 10
            resto = soma %11
            if resto == 10:
                resto = 0

            if resto == int(cpf[9]):
                c = 11
                soma2 = 0
                for i in cpf[0:10]:
                    soma2 += int(i)*c
                    resto2 = soma2%11
                    if resto2 == 10:
                        resto2 = 0
                    if resto2 == int(cpf[10]):
                        return True


            else:
                return False
            
        
    def valida_data_nascimento(self, data_nascimento):
        data_nascimento = data_nascimento.replace('/', '')
        dia = data_nascimento[0:2]
        mes = data_nascimento[2:4]
        ano = data_nascimento[4:]

        mes30 = [4, 6, 9, 11]
        if int(mes) > 12:
            return False
        if int(dia) > 31:
            return False
        if int(mes) in mes30:
            if int(dia) > 30:
                return False
        if int(mes) == 2:
            if (int(ano)%4==0) and int(dia)>29:
                return False
            elif int(dia) > 28:
                return False
        return True
            

    def formata_cpf(self, cpf):
        cpf = cpf.replace('.', '').replace('-', '')
        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return cpf


    def formata_data_nascimento(self, data_nascimento):
        data_nascimento = data_nascimento.replace('/', '')
        data_nascimento = data_nascimento[0:2] + '/' + data_nascimento[2:4] + '/' + data_nascimento[4:]
        return data_nascimento


    def cadastrar_pessoa(self, nome, cpf, data_nascimento, email, endereco):
        pes = DaoPessoa.ler()

        cpf = ControllerPessoa().formata_cpf(cpf)
        data_nascimento = ControllerPessoa().formata_data_nascimento(data_nascimento)

        for i in pes:
            if i.cpf == cpf:
                return print('Cpf já cadastrado')
        
        if ControllerPessoa().valida_cpf(cpf) and ControllerPessoa().valida_data_nascimento(data_nascimento):
            pessoa = Pessoa(nome, cpf, data_nascimento, email, endereco)
            DaoPessoa.salvar(pessoa)
            print('Cliente cadastrado com sucesso')
        else:
            print('Insira informações válidas.')


    def alterar_pessoa(self, cpf, email, endereco):
        pes = DaoPessoa.ler()
        existe = False

        for i in pes:
            if i.cpf == cpf:
                existe = True
                i.email = email
                i.endereco = endereco

        if existe:
            with open('clientes.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in pes:
                DaoPessoa.salvar(i)
                print('Dados atualizados com sucesso')
        else:
            print('Cliente não encontrado')


    def remover_pessoa(self, cpf):
        pes = DaoPessoa.ler()
        existe = False

        for i in pes:
            if i.cpf == cpf:
                existe = True
                pes.pop(pes.index(i))
                print('Cliente removido com sucesso')

        if existe:
            with open('clientes.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in pes:
                DaoPessoa.salvar(i)
                
        else:
            print('Cliente não encontrado')


    def imprimir_clientes(self):
        pes = DaoPessoa.ler()
        print(f'Nome | CPF | Data de Nascimento | Email | Endereco')
        print('-'*80)
        for i in pes:
            print(f'{i.nome} | {i.cpf} | {i.data_nascimento} | {i.email} | {i.endereco}')

        
class ControllerFuncionario:


    def cadastrar_funcionario(self, clt, nome, cpf, data_nascimento, email, endereco):
        func = DaoFuncionario.ler()

        cpf = ControllerPessoa().formata_cpf(cpf)
        data_nascimento = ControllerPessoa().formata_data_nascimento(data_nascimento)

        for i in func:
            if i.clt == clt or i.cpf == cpf:
                
                return print('Funcionário já cadastrado')
        if len(func) == 0:
            id_funcionario = 101
        else:
            id_funcionario = int(func[len(func)-1].id_funcionario) + 1
        
        if ControllerPessoa().valida_cpf(cpf) and ControllerPessoa().valida_data_nascimento(data_nascimento):
            funcionario = Funcionario(str(id_funcionario), clt, nome, cpf, data_nascimento, email, endereco)
            DaoFuncionario().salvar(funcionario)
            print(f'ID de funcionário cadastrada: {str(id_funcionario)}')
        else:
            print('Insira informações válidas')


    def alterar_funcionario(self, id_funcionario, email, endereco):
        func = DaoFuncionario.ler()
        existe = False

        for i in func:
            if i.id_funcionario == id_funcionario:
                i.email = email
                i.endereco = endereco
                print('Dados atualizados com sucesso')
                existe = True

        if existe:
            with open('funcionarios.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in func:
                DaoFuncionario.salvar(i)
        else:
            print('Funcionário não cadastrado')


    def remover_funcionario(self, id_funcionario):
        func = DaoFuncionario.ler()
        existe = False

        for i in func:
            if i.id_funcionario == id_funcionario:
                func.pop(func.index(i))
                existe = True
                print('Funcionário removido com sucesso')
        
        if existe:
            with open('funcionarios.txt', 'r+')as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in func:
                DaoFuncionario.salvar(i)
        else:
            print('ID de funcionário inválida')


    def imprimir_funcionarios(self):
        func = DaoFuncionario.ler()
        print(f'Id | CLT | Nome | CPF | Data de Nascimento | Email | Endereço')
        print('-'*80)
        for i in func:
            print(f'{i.id_funcionario} | {i.clt} | {i.nome} | {i.cpf} | {i.data_nascimento} | {i.email} | {i.endereco}')


class ControllerFornecedor:

    def valida_cnpj(self, cnpj):
        nMultiplicadores1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma1 = 0
        #Aqui nós limpamos o cnpj dos caracteres especiais
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if len(cnpj) != 14:
            return False

        #Começa a validação do primeiro número do CNPJ
        for i, n in enumerate(cnpj[0:12]):
            soma1 += int(n) * nMultiplicadores1[i]
        resto1 = soma1 % 11
        if resto1 == 1 or resto1 == 0:
            if cnpj[12] != 0:
                return False
            else:
                if cnpj[12] != (11-resto1):
                    return False
        
        #Validação do segundo número
        nMultiplicadores2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma2 = 0
        for i, n in enumerate(cnpj[0:13]):
            soma2 += int(n) * nMultiplicadores2[i]
        resto2 = soma2 % 11
        if resto2 == 1 or resto2 == 0:
            if cnpj[12] != 0:
                return False
            else:
                if cnpj[13] != (11-resto2):
                    return False
        #Caso passe pelas validações retorna True
        return True            

    def formatar_cnpj(self, cnpj):
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        cnpj = cnpj[0:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]
        return cnpj

    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        forn = DaoFornecedor.ler()
        
        cnpj = ControllerFornecedor().formatar_cnpj(cnpj)

        for i in forn:
            if i.cnpj == cnpj:
                return print('CNPJ já cadastrado')
            
        if ControllerFornecedor().valida_cnpj(cnpj):
            fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
            DaoFornecedor.salvar(fornecedor)
            print('Fornecedor cadastrado com sucesso')
        else:
            print('Insira um CNPJ válido')

    
    def alterar_fornecedor(self, cnpj, telefone, categoria):
        forn = DaoFornecedor.ler()
        existe = False
        cnpj = ControllerFornecedor().formatar_cnpj(cnpj)

        for i in forn:
            if i.cnpj == cnpj:
                existe = True
                i.telefone = telefone
                i.categoria = categoria
                print('Dados atualizados com sucesso')
                
        if existe:
            with open('fornecedor.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)

            for i in forn:
                DaoFornecedor().salvar(i)
        else:
            print('CNPJ não cadastrado')

    def remover_fornecedor(self, cnpj):
        forn = DaoFornecedor.ler()
        existe = False

        cnpj = ControllerFornecedor().formatar_cnpj(cnpj)

        for i in forn:
            if i.cnpj == cnpj:
                forn.pop(forn.index(i))
                existe = True
                print('Fornecedor removido com sucesso')
        
        if existe:
            with open('fornecedor.txt', 'r+') as arq:
                arq.truncate(0)
                arq.seek(0)
            for i in forn:
                DaoFornecedor.salvar(i)
        else:
            print('CNPJ não cadastrado')

    
    def imprimir_fornecedor(self):
        forn = DaoFornecedor.ler()

        print('Nome | CNPJ | Telefone | Categoria')
        print('-'*80)
        for i in forn:
            print(f'{i.nome} | {i.cnpj} | {i.telefone} | {i.categoria}')


class ControllerVendas:

    def cadastrar_venda(self, id_funcionario, cpf_cliente):
        from time import sleep
        func_list = DaoFuncionario.ler()
        func_existe = False
        client_list = DaoPessoa.ler()
        client_existe = False
        est = DaoEstoque.ler()
        prod_existe = False
        cpf_cliente = ControllerPessoa().formata_cpf(cpf_cliente)

        #Checa se o funcionário está cadastrado
        for i in func_list:
            if i.id_funcionario == id_funcionario:
                func_existe = True
                funcionario = Funcionario(id_funcionario, i.clt, i.nome, i.cpf, i.data_nascimento, i.email, i.endereco)
        if not func_existe:
            return print('Funcionário não cadastrado')
        
        #Checa se o cliente está cadastrado, se não inicia o cadastro
        for i in client_list:
            if i.cpf == cpf_cliente:
                client_existe = True
                cliente = Pessoa(i.nome, i.cpf, i.data_nascimento, i.email, i.endereco)
        if not client_existe:
            print('Cliente não cadastrado. Iniciando cadastro de cliente... ')
            sleep(2)
            ControllerPessoa().cadastrar_pessoa(
                input('Nome: '),
                input('CPF: '),
                input('Data de Nascimento: '),
                input('Email: '),
                input('Endereço: ')
            )

        total_venda = []
        carrinho = ''
        total_qtd = []

        #Criação do loop infinito para cadastro de produtos
        while True:
            decisao = input('Cadastro de produtos: (Pressione ENTER para continuar e Q para sair)')
            #Se pressionar Q o loop é interrompido. Caso o carrinho esteja vazio o loop continua.
            if decisao == 'Q' or decisao == 'q':
                if len(carrinho) == 0:
                    print('Carrinho vazio. Cadastre pelo menos um item.')
                else:
                    break
            nome_produto = input('Nome do produto: ')
            quantidade = input('Quantidade: ')
            
            #Checa se o produto está cadastrado e se a quantidade é suficiente.
            for i in est:
                if i.produto.nome == nome_produto:
                    prod_existe = True
                    produto = Produto(i.produto.nome, i.produto.preco, i.produto.categoria)
                    while int(i.quantidade) < int(quantidade):
                        print(f'Quantidade insuficiente no estoque. Quantidade no estoque:{i.quantidade}')
                        quantidade = input('Insira nova quantidade: ')

                    #Atualiza o estoque retirando a quantidade comprada
                    ControllerEstoque().atualizar_estoque(nome_produto, quantidade, False)

            
            if not prod_existe:
                print('Produto indisponível, por favor cadastre o produto no estoque.')
            else:
                total_venda.append(int(quantidade) * float(produto.preco))
                carrinho += f'{produto.nome} - R${produto.preco} - {quantidade},'
                total_qtd.append(quantidade)
            ControllerVendas().visor_caixa(carrinho, total_qtd, total_venda)
            sleep(1)

        venda = Venda(carrinho, funcionario.id_funcionario, cliente.cpf, str(sum(total_venda)))
        DaoVendas.salvar(venda)
        print('Venda cadastrada com sucesso!')
    

    def visor_caixa(self, carrinho, total_qtd, total_venda):
        print('\n')
        print('-'*40)
        carrinho = list(carrinho.split(','))
        for i, _ in enumerate(carrinho):
            if i < len(carrinho)-1:
                print(f'{i+1} - {carrinho[i]} - {total_qtd[i]} - R${total_venda[i]}')
        print(f'Total: {sum(total_venda):>40}')
        print('-'*40)
        print('\n')


    def limpa_lista(self, lista):
        lista = list(map(lambda x: x.replace('[', ''), lista))
        lista = list(map(lambda x: x.replace(']', ''), lista))
        lista = list(map(lambda x: x.replace('\'', ''), lista))
        lista = list(map(lambda x: x.split(','), lista))
        return lista


    def relatorio_geral(self):
        vendas = DaoVendas.ler()
        func = DaoFuncionario.ler()
        cliente = DaoPessoa.ler()
        vendedor = comprador = ''

        #começa a impressão
        print('\n')
        print(f'{"Relatório Geral de vendas":^80}')
        print('-'*80)
        print('Vendedor | Cliente | Total | Data | Produto | Preço | Quantidade')
        print('-'*80)
        for i in vendas:
            for j in func:
                if i.vendedor == j.id_funcionario:
                    vendedor = j.nome
            for h in cliente:
                if i.comprador == h.cpf:
                    comprador = h.nome
            i.itens_vendidos = i.itens_vendidos.split(',')
            data = datetime.strptime(i.data.split('.')[0], "%Y-%m-%d %H:%M:%S")
            frase = f'{vendedor} | {comprador} | R${float(i.quantidade_vendida):.2f} | {data.strftime("%d/%m/%Y %H:%M")} | {i.itens_vendidos[0]}'
            print(frase)
            for k in i.itens_vendidos[1:]:
                print(f'{" "*(len(frase)-len(i.itens_vendidos[0])-2)}| {k}')     
            
            


    def relatorio_por_data(self, data_inicio, data_fim = datetime.now()):
        vendas = DaoVendas.ler()
        func = DaoFuncionario.ler()
        cliente = DaoPessoa.ler()
         
        vendedor = comprador = ''
        #incluo 00:00 para contar o dia inteiro
        data_inicio += ' 00:00'
        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y %H:%M')
        #incluo 23:59 para contar o último dia todo
        data_fim += ' 23:59'
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y %H:%M')

        #começa a impressão
        print('\n')
        print(f'{"Relatório Geral de vendas":^80}')
        print('-'*80)
        print('Vendedor | Cliente | Total | Data | Produto | Preço | Quantidade')
        print('-'*80)
        for i in vendas:
            data = datetime.strptime(i.data.split('.')[0], "%Y-%m-%d %H:%M:%S")
            if data >= data_inicio and data <= data_fim:
                for j in func:
                    if i.vendedor == j.id_funcionario:
                        vendedor = j.nome
                for h in cliente:
                    if i.comprador == h.cpf:
                        comprador = h.nome
                i.itens_vendidos = i.itens_vendidos.split(',')
                
                frase = f'{vendedor} | {comprador} | R${float(i.quantidade_vendida):.2f} | {data.strftime("%d/%m/%Y %H:%M")} | {i.itens_vendidos[0]}'
                print(frase)
                for k in i.itens_vendidos[1:]:
                    print(f'{" "*(len(frase)-len(i.itens_vendidos[0])-2)}| {k}')     


    def relatorio_mais_vendidos(self):
        vendas = DaoVendas.ler()
        produtos = []
        valores = []

        for i in vendas:
            i.itens_vendidos = i.itens_vendidos.split(',')
            for j in i.itens_vendidos:
                if j != '':
                    j = j.strip()
                    j = j.split(' - ')
                    if j[0] not in produtos:
                        produtos.append(j[0])
                        valores.append(int(j[2]))
                    else:
                        valores[produtos.index(j[0])] += int(j[2])
        print(f'{"Mais Vendidos":^30}')
        print('-'*30)
        print(f'{"Produto":<20}{"Quantidade"}')
        print('-'*30)
        
        for i in range(0, 5 if len(produtos)>5 else len(produtos)):
            mais_vendido_num = 0

            for j in valores:
                if j >= mais_vendido_num:
                    mais_vendido_num = j
            mais_vendido = produtos[valores.index(mais_vendido_num)]

            print(f'{mais_vendido}{"-":^20}{mais_vendido_num:}')
            produtos.pop(produtos.index(mais_vendido))
            valores.pop(valores.index(mais_vendido_num))
        
            
    def relatorio_clientes_mais_compraram(self):
        vendas = DaoVendas.ler()
        clientes = DaoPessoa.ler()
        cpf_clientes = []
        gastos_clientes = []
        nome_clientes = []

        for i in vendas:
            if i.comprador not in cpf_clientes:
                cpf_clientes.append(i.comprador)
                gastos_clientes.append(float(i.quantidade_vendida))
            else:
                gastos_clientes[cpf_clientes.index(i.comprador)] += float(i.quantidade_vendida)
            for j in clientes:
                if j.nome not in nome_clientes:
                    nome_clientes.append(j.nome)

        print(f'{"Mais Compraram":^30}')
        print('-'*30)
        print(f'{"Cliente":<20} | {"CPF":^11} | Total')
        print('-'*30)    

        for i in range(1, 5 if len(cpf_clientes) >= 5 else len(cpf_clientes)+1):
            maior = 0
            
            for j in gastos_clientes:
                if j > maior:
                    maior = j
            cliente_mais_comprou = nome_clientes[gastos_clientes.index(maior)]
            cpf_mais_comprou = cpf_clientes[gastos_clientes.index(maior)]

            print(f'{cliente_mais_comprou} | {cpf_mais_comprou} | R${maior}')
            nome_clientes.pop(gastos_clientes.index(maior))
            cpf_clientes.pop(gastos_clientes.index(maior))
            gastos_clientes.pop(gastos_clientes.index(maior))

