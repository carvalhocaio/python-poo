import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_do_programa():
    """
    Exibe o nome do programa no console usando arte ASCII.
    """
    # https://fsymbols.com/
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    """
    Exibe as opções disponíveis no menu principal do programa.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Exibe uma mensagem de finalização do aplicativo.
    """
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    """
    Solicita uma entrada do usuário para retornar ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu')
    main()

def opcao_invalida():
    """
    Notifica o usuário que uma opção inválida foi selecionada e retorna ao menu principal.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe um texto formatado como subtítulo, com linhas acima e abaixo do texto.
    
    Args:
        texto (str): O subtítulo a ser exibido.
    """
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Solicita os dados do restaurante ao usuário e o adiciona à lista de restaurantes.
    
    Inputs solicitados:
        - Nome do restaurante
        - Categoria do restaurante
    
    Efeitos:
        - Adiciona um novo restaurante à lista `restaurantes`.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Exibe todos os restaurantes cadastrados com suas categorias e estados.
    
    Efeitos:
        - Exibe a lista de restaurantes formatada no console.
    """
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Alterna o estado de um restaurante (ativo/desativado) com base no nome fornecido pelo usuário.
    
    Inputs solicitados:
        - Nome do restaurante
    
    Efeitos:
        - Altera o atributo `ativo` do restaurante correspondente.
        - Exibe uma mensagem indicando o sucesso ou a falha da operação.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Lê a opção do usuário e executa a ação correspondente.
    
    Efeitos:
        - Invoca a função apropriada com base na opção escolhida pelo usuário.
        - Notifica o usuário em caso de opção inválida.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """
    Função principal que inicia o aplicativo.
    
    Efeitos:
        - Limpa a tela.
        - Exibe o nome do programa e as opções disponíveis.
        - Lida com a navegação do menu principal.
    """
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
