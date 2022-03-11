

def menu():
    # Escolhas
    opcao = int(input('''
    ==============================================
                        Agenda 
    MENU:    
    
    [1] CADASTRAR CONTATO
    [2] LISTAR CONTATOS
    [3] DELETAR CONTATO
    [4] BUSCAR CONTATO PELO NOME
    
    ==============================================
    ESCOLHA UMA OPÇÃO ACIMA: '''))

    if opcao == 1:
        CadastrarContato()
    elif opcao == 2:
        ListarContato()
    elif opcao == 3:
        DeletarContato()
    elif opcao == 4:
        BuscarPeloNome()

    # EscolhaInvalida
    if opcao > 4:
        erro()


def erro():
    opcao2 = int(input('''
        
        
    ==============================================
                     OPÇÃO INVALIDA
           [1]Voltar                [2]Sair
    ==============================================
                      '''))

    if opcao2 == 1:
        limpar()
        menu()
    elif opcao2 == 2:
        quit()

def voltar():
    opcao3 = int(input('''


        ==============================================
                    Deseja tentar novamente?
           [1]Sim         [2]Menu           [3]Sair
        ==============================================
                          '''))

    if opcao3 == 1:
        limpar()
        menu()
    elif opcao3 == 2:
        menu()
    elif opcao3 == 3:
        quit()


def CadastrarContato():
    print('''
    ==============================================
                Cadastrar contato''')

    try:
        id = int(input("Digite o ID do contato: "))
    except ValueError:
        print("Oops! esse numero não é valido tente novamente")

    Name = input('\nDigite o nome do contato: ')

    Number = int(input('\nDigite o Numero do Contato com o DDD: '))

    email = input('Digite o email do Contato: ')

    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{id};{Name};{Number};{email}\n'
        ##if dados
        agenda.write(dados)
        agenda.close()
        print('''
             Contato Gravado Com sucesso
                ''')
    except:
        print('ERRO na gravação do contato')
    menu()

def ListarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()
    quit()

def DeletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ")
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'contato deletado com sucesso')
    ListarContato()



def BuscarPeloNome():
    nome=input(f'digite o nome a ser procurado: ').upper()
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)

    agenda.close()
    voltar()



def limpar():
    print("\n" * 130)
def pergunta():
    print()


menu()
