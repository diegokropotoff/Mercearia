import controller
import os.path
from time import sleep

def cria_arquivo(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.writelines('')


cria_arquivo('categorias.txt', 'fornecedor.txt', 'estoque.txt', 'clientes.txt', 'funcionarios.txt', 'vendas.txt')


if __name__ == '__main__':
    while True:
        print('\n')
        sleep(0.5)
        print('Escolha que menu deseja acessar: ')
        menu = int(input(
            '1 - Vendas\n'
            '2 - Categoria\n'
            '3 - Estoque\n'
            '4 - Fornecedor\n'
            '5 - Cliente\n'
            '6 - Funcionário\n'
            '7 - Sair\n'
        ))
        sleep(0.3)

        if menu == 1:
            ven = controller.ControllerVendas()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - CAIXA\n'
                    '2 - Relatório Geral de Vendas\n'
                    '3 - Relatório de Vendas por Data\n'
                    '4 - Produtos mais vendidos\n'
                    '5 - Clientes que mais compraram\n'
                    '6 - Voltar\n'
                ))
                sleep(0.3)

                if decisao == 1:
                    vendedor = input('Digite o ID de funcionário: ')
                    cliente = input('Digite o CPF do cliente: ')
                    ven.cadastrar_venda(vendedor, cliente)

                elif decisao == 2:
                    ven.relatorio_geral()
                
                elif decisao == 3:
                    pes = controller.ControllerPessoa()
                    data_inicio = pes.formata_data_nascimento(input('Insira a data de início(DD/MM/YYYY): '))
                    data_fim = pes.formata_data_nascimento(input('Insira a data final(DD/MM/YYYY): '))
                    if data_fim == '':
                        ven.relatorio_por_data(data_inicio)
                    else:
                        ven.relatorio_por_data(data_inicio, data_fim)

                elif decisao == 4:
                    ven.relatorio_mais_vendidos()

                elif decisao == 5:
                    ven.relatorio_clientes_mais_compraram()

                elif decisao == 6:
                    break

                else:
                    print('Opção inválida')
        
        elif menu == 2:
            cat = controller.ControllerCategoria()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - Cadastrar Categoria\n'
                    '2 - Alterar Categoria\n'
                    '3 - Remover Categoria\n'
                    '4 - Listar Categorias\n'
                    '5 - Voltar\n'
                ))
                if decisao == 1:
                    categoria = input('Digite o nome da categoria: ')
                    cat.cadastrar_categoria(categoria)

                elif decisao == 2:
                    categoria = input('Digite o nome da categoria que deseja alterar: ')
                    nova_categoria = input('Digite o nome da nova categoria: ')
                    cat.alterar_categoria(categoria, nova_categoria)

                elif decisao == 3:
                    categoria = input('Digite o nome da categoria que deseja remover: ')
                    cat.remover_categoria(categoria)

                elif decisao == 4:
                    cat.imprimir_categorias()

                elif decisao == 5: 
                    break

                else:
                    print('Opção inválida')
        
        elif menu == 3:
            est = controller.ControllerEstoque()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - Cadastrar produto\n'
                    '2 - Alterar produto\n'
                    '3 - Remover produto\n'
                    '4 - Acrescentar quantidade ao produto\n'
                    '5 - Listar Estoque\n'
                    '6 - Voltar\n'
                ))
                if decisao == 1:
                    nome = input('Nome: ')
                    preco = input('Preço: R$').replace(',', '.')
                    categoria = input('Categoria: ')
                    quantidade = input('Quantidade: ')
                    est.cadastrar_produto(nome, preco, categoria, quantidade)

                elif decisao == 2:
                    nome = input('Digite o nome do produto que deseja alterar: ')
                    novo_nome = input('Digite o nome do novo produto: ')
                    novo_preco = input('Digite o preço do  novo produto: R$').replace(',', '.')
                    novo_categoria = input('Digite a categoria do novo produto: ')
                    nova_quantidade = input('Digite a quantidade do novo produto: ')
                    est.alterar_produto(nome, novo_nome, novo_preco, nova_categoria, nova_quantidade)

                elif decisao == 3:
                    nome = input('Digite o nome do produto a ser removido: ')
                    est.remover_produto(nome)

                elif decisao == 4:
                    nome = input('Nome do produto: ')
                    quantidade = input('Informe a quantidade para adicionar: ')
                    est.atualizar_estoque(nome, quantidade)

                elif decisao == 5:
                    est.imprimir_estoque()

                elif decisao == 6:
                    break

                else:
                    print('Opção inválida')

        elif menu == 4:
            forn = controller.ControllerFornecedor()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - Cadastrar Fornecedor\n'
                    '2 - Alterar Fornecedor\n'
                    '3 - Remover Fornecedor\n'
                    '4 - Listar Fornecedores\n'
                    '5 - Voltar\n'
                ))
                if decisao == 1:
                    nome = input('Nome: ')
                    cnpj = input('CNPJ: ')
                    telefone = input('Telefone: ')
                    categoria = input('Categoria: ')
                    forn.cadastrar_fornecedor(nome, cnpj, telefone, categoria)

                elif decisao == 2:
                    cnpj = input('CNPJ do fornecedor que deseja alterar: ')
                    telefone = input('Novo Telefone: ')
                    categoria = input('Nova Categoria: ')
                    forn.alterar_fornecedor(cnpj, telefone, categoria)

                elif decisao == 3:
                    cnpj = input('CNPJ do fornecedor a ser removido: ')
                    forn.remover_fornecedor(cnpj)
                
                elif decisao == 4:
                    forn.imprimir_fornecedor()

                elif decisao == 5:
                    break
                    
                else:
                    print('Opção inválida')

        elif menu == 5:
            cli = controller.ControllerPessoa()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - Cadastrar Cliente\n'
                    '2 - Alterar Cliente\n'
                    '3 - Remover Cliente\n'
                    '4 - Listar Cliente\n'
                    '5 - Voltar\n'
                ))
                if decisao == 1:
                    nome = input('Nome: ')
                    cpf = input('CPF: ')
                    data_nascimento = input('Data de Nascimento(DD/MM/YYYY): ')
                    email = input('Email: ')
                    endereco = input('Endereço: ')
                    cli.cadastrar_pessoa(nome, cpf, data_nascimento, email, endereco)

                elif decisao == 2:
                    cpf = input('CPF do cliente para alterações: ')
                    email = input('Novo Email: ')
                    endereco = input('Novo Endereço: ')
                    cli.alterar_pessoa(cpf, email, endereco)

                elif decisao == 3:
                    cpf = input('CPF do cliente a ser removido: ')
                    cli.remover_pessoa(cpf)
                
                elif decisao == 4:
                    cli.imprimir_clientes()

                elif decisao == 5:
                    break

                else:
                    print('Opção inválida')

        elif menu == 6:
            func = controller.ControllerFuncionario()
            while True:
                print('\n')
                decisao = int(input(
                    '1 - Cadastrar Funcionário\n'
                    '2 - Alterar Funcionário\n'
                    '3 - Remover Funcionário\n'
                    '4 - Listar funcionários\n'
                    '5 - Voltar\n'
                ))

                if decisao == 1:
                    clt = input('CLT: ')
                    nome = input('Nome: ')
                    cpf = input('CPF: ')
                    data_nascimento = input('Data de Nascimento: ')
                    email = input('Email: ')
                    endereco = input('Endereço: ')
                    func.cadastrar_funcionario(clt, nome, cpf, data_nascimento, email, endereco)

                elif decisao == 2:
                    id_funcionario = input('Insira a ID de funcionário para alterações: ')
                    email = input('Novo Email: ')
                    endereco = input('Novo endereço: ')
                    func.alterar_funcionario(id_funcionario, email, endereco)

                elif decisao == 3:
                    id_funcionario = input('ID de funcionário para remoção: ')
                    func.remover_funcionario()

                elif decisao == 4:
                    func.imprimir_funcionarios()

                elif decisao == 5:
                    break

                else:
                    print('Opção inválida')

        elif menu == 7:
            break

        else:
            print('Opção inválida')