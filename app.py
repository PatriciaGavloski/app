import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print("""
     Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
       """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
  os.system('cls')
  print('Ａｐｌｉｃａｔｉｖｏ Ｆｉｎａｌｉｚａｄｏ\n')

def opcao_invalida():
    print('Opção Inválida\n')
    input('Digite qualquer tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('\nDigite qualquer tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Lista dos Restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('\nDigite qualquer tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()