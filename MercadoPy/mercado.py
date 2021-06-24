from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []                         # cria lista com classe produtos
carrinho: List[Dict[Produto, int]] = []              # cria lista com dicionarios

def main() -> None:
    menu()

def menu() -> None:
    print('-----------------------------------------------------')
    print('---------------------Bem Vindx-----------------------')
    print('--------------------ManeiraStore---------------------')
    print('-----------------------------------------------------\n')

    print('Selecione uma das opções: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção invalida')
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('-------------------')

    nome: str = input('Informe o nome do produto: ')                 # pega do usuario nome do produto
    preco: float = float(input('Informe o preço do produto: '))      # pega do usuario preço do produto

    produto: Produto = Produto(nome, preco)                          # adiciona atributo nome e preço no produto

    produtos.append(produto)                                          # add produto na lista produto

    print(f'O produto {produto.nome} foi cadastrado com sucesso')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:                      # se lista nao for vazia executa
        print('Listagem de Produtos')
        print('--------------------')
        for produto in produtos:               # para produto na lista produtos
            print(produto)                     # imprima cada produto
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não há produtos cadastrados')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:                     # se lista nao for vazia executa
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print(f'--------------------Produtos Disponíveis---------------------')
        for produto in produtos:               # para produto na lista produtos
            print(produto)                     # imprime cada produto
            print(f'--------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())              # pede codigo para fazer a compra

        produto: Produto = pega_produto_por_codigo(codigo)
        # define produto de acordo com código digitado através da função pega produto por codigo

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:                     # para item no carrinho
                    quantidade: int = item.get(produto)  # pega mais item ja existente no carrinho
                    if quantidade:
                        item[produto] = quantidade + 1    # adiciona mais um item do mesmo ao carrinho
                        print(f'O produto {produto.nome} agora possui {quantidade + 1} unidades no carrinho')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:                     # se nao possui item no carrinho ainda
                    prod = {produto: 1}                     # prod é igual a produto
                    carrinho.append(prod)                    # add prod no dicionario carrinho
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:                          # se carrinho estiver vazio
                item = {produto: 1}        # item é igual produto
                carrinho.append(item)      # add item no dicionario carrinho
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:               # codigo nao foi encontrado
            print(f'O produto com código {codigo} não foi encontrado')
            sleep(2)
            menu()
    else:     # não existe nenhum produto cadastrado
        print('Não há produtos cadastrados ainda')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos de Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('----------------------------')
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print(f'Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não há produtos no carrinho')
    sleep(2)
    exit()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(f'Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
                menu()
    else:
        print(f'Ainda não há produtos no carrinho')
    sleep(2)
    menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()