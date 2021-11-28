'''
    !CARRINHO DE COMPRAS!
'''
#todo --> Passo 4°: Criar uma função que retorne um valor booleano (true ou false), para confirmação do produto em estoque
def produto_em_estoque(produtos, produto):
    return produtos[produto]['quantidade'] > 0


#todo --> Passo 3°: Criar uma função com os três parâmentros, sendo o 1° - carrinho, 2° - os produtos do array e o 3° id do produto e com as condições:
def add_produto(carrinho, produtos, produto):
    '''
    1°
        - se o produto estiver no carrinho (pegando o id do produto), verificar se está em estoque
        - se o produto estiver em estoque, adiciona (+1) produto dentro do carrinho e retirar (-1) produto do array/estoque (produtos)
        - se não estiver em estoque, emitir um aviso para o usuário
        
    2°
        - se o produto não estiver no carrinho, verificar se está em estoque
        - se o produto estiver em estoque, vai criar um novo objeto (que no caso, têm os mesmos valores do produto selecionado) e vai retirar (-1) produto do array/estoque (produtos)
        - se não estiver em estoque, emitir um aviso para o usuário
    '''
    if produto in carrinho.keys():
        if produto_em_estoque(produtos, produto):
            carrinho[produto]['quantidade'] += 1
            carrinho[produto]['valor'] += produtos[produto]['valor']

            produtos[produto]['quantidade'] -= 1

        else:
            print('Produto esgotado!')

    else:
        if produto_em_estoque(produtos, produto):
            carrinho[produto] = {
                'nome': produtos[produto]['nome'],
                'valor': produtos[produto]['valor'],
                'quantidade': 1
            }

            produtos[produto]['quantidade'] -= 1

        else:
            print('Produto esgotado!')


#todo --> Passo 5°: Criar uma função para imprimir todos os valores do Array - Produtos
def mostra_produtos(produtos):
    print('Produtos:')
    '''
    Laço "for", para pegar todos os valores que devem ser informados para o usuário
    (e não precisar digitar muitos trechos de código com vários "print's")
    '''
    for id_produto in produtos.keys():
        print(
            f'\tProduto: {produtos[id_produto]["nome"]}\n\tValor: {produtos[id_produto]["valor"]}\n\tEstoque: {produtos[id_produto]["quantidade"]}')


#todo --> Passo 6°: Cria uma função para imprimir todos os valores do Array - Carrinho
def mostra_carrinho(carrinho):
    print('Carrinho:')
    '''
    Laço "for", para pegar todos os valores que devem ser informados para o usuário
    (e não precisar digitar muitos trechos de código com vários "print's")
    '''
    for id_produto in carrinho.keys():
        print(
            f'\tProduto: {carrinho[id_produto]["nome"]}\n\tValor: {carrinho[id_produto]["valor"]}\n\tQuantidade: {carrinho[id_produto]["quantidade"]}')


#todo --> Passo 1°: Criando um array com dois objetos, identificados por um id "0" e "1"
produtos = {
    0: {
        'nome': 'Air Jordan 1 Vermelho',
        'valor': 1200,
        'quantidade': 10
    },

    1: {
        'nome': 'Air Jordan Laranja',
        'valor': 1000,
        'quantidade': 5
    }
}


#todo --> Passo 2°: Criando o array do carrinho, vazio, pois, o produto será adicionado somente se o usuário quiser.
carrinho = {

}


#todo --> Passo 7°: Criando um laço, para enquanto for verdade, ser adicionado a pergunta ao usuário para adicionar mais itens ou finalizar a compra
while True:
    mostra_produtos(produtos)
    mostra_carrinho(carrinho)

    adicionar = input('Adicionar produto (s/n): ').lower() #!Passando tudo para 'lowercase()', pois caso o usuário digite 'S' ou 's' não dar conflito

#? --> Passo 8: Criando uma última condição para finalizar ou continuar o programa
    #! Se for digitado 's', o programa/compra condinua e pergunta o id do produto, caso for digitado 'n', o programa/compra é finalizado.
    if adicionar == 's':

        id_produto = int(input('ID do Produto: '))

        add_produto(carrinho, produtos, id_produto)

    else:
        
        break
