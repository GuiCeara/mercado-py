from cadastro import Cadastro
from perfil import Perfil
from listaProdutos import ListaProdutos
from produtos import Produtos
session = ''
sessionName = ''

def start():

    esc = str(input('\n*****Mercado*****\n' 'Cadastrar (1)\n' 'Entrar (2)\n' 'Menu (3)\n' 'Sair (4)\n' 'Digite: '))

    if esc == '1':
        cadastrar()
    elif esc == '2':
        login()
    elif esc == '3':
        menu()
    elif esc == '4':
        print('\nSaíndo...\n')
        exit()
    else:
        print('Escolha Inválida.')
    
def cadastrar():
    print('\n*****Cadastro*****')
    user = str(input('User: '))
    while len(user) < 4:
        print('Usuário Inválido, apenas acima de 3 caracteres.')
        user = str(input('User: '))
    senha = str(input('Senha: '))
    while len(senha) > 16 or len(senha) < 4:
        print('Senha Inválida.')
        senha = str(input('Senha: '))
    objCadastrar = Cadastro(user, senha)
    if objCadastrar.cadastrarVerify() == True:
        objCadastrar.cadastrarC()

def login():
    global session, sessionName
    print('\n*****Entrar*****')
    user = str(input('User: '))
    while len(user) < 4:
        print('Usuário Inválido, apenas acima de 3 caracteres.')
        user = str(input('User: '))
    senha = str(input('Senha: '))
    while len(senha) > 16 or len(senha) < 4:
        print('Senha Inválida.')
        senha = str(input('Senha: '))
    checkS = 'NULL'
    checkU = 'NULL'
    objLogin = Perfil(user, senha, checkS, checkU)
    if objLogin.perfilVerify() == True:
        session = 'start'
        sessionName = objLogin.user
        print(f'\nSeja bem vindo "{sessionName}"')
        menu()
    else:
        print('Usuário ou senha incorreta.')
        start()

def menu():
    esc = str(input('\n*****MENU*****\n' 'Perfil (1)\n' 'Catálogo (2)\n' 'Comprar Produtos (3)\n' 'Sair (4)\n' 'Digite: '))
    if esc == '1':
        perfil()
    elif esc == '2':
        print('\n*****Catálogo do Mercado*****\n')
        objLista = ListaProdutos
        if objLista.catalogo() == True:
            menu()
    elif esc == '3':
        cProdutos()
    elif esc == '4':
        print('\nSaíndo...\n')
        exit()
    else:
        print('Escolha Inválida.')

def cProdutos():
    print('\n*****Comprar Produtos*****\n')
    try:
        id = int(input('Id do Produto: '))
        quantidade = int(input('Quantidade do Produto: '))
        if session != 'start':
            print('Ops... usuário não logado!')
            start()
        else:
            user = sessionName
            objProdutos = Produtos(id, quantidade, user)
            if objProdutos.verifyProdutos() == True:
                print('\nDetalhes do Pedido:\n' f'Nome do produto: {objProdutos.nomeProduto}\n' f'Quantidade: {objProdutos.quantidade}\n' f'Valor do produto: R${objProdutos.valorProduto}\n' f'Valor total: R${objProdutos.total}\n')
                esc = str(input('Para confirmar s/n\n')).lower()
                if esc == 's':
                    print('pedido confirmado!')
                    if objProdutos.confirmProdutos() == True:
                        objProdutos.addHistoric()
                        menu()
                else:
                    menu()
            else:
                print('Produto fora de estoque ou inexistente.')
    except:
        print('Houve algum erro...')
        menu()
    
def perfil():
    print(f'\n*****Perfil de {sessionName}*****\n')
    esc = str(input('Alterar nome (1)\n' 'Alterar senha (2)\n' 'Histórico de pedidos (3)\n' 'Sair (4)\n' 'Digite: '))
    if esc == '1':
        perfilUser()
    elif esc == '2':
        perfilSenha()
    elif esc == '3':
        perfilHistorico()
    elif esc == '4':
        print('\nSaíndo...\n')
        exit()   
    else:
        print('Escolha Inválida.')

def perfilUser():
    global sessionName
    checkU = str(input('Digite seu novo nome: '))
    while len(checkU) < 1:
        print('Usuário Inválido, apenas acima de 3 caracteres.')
        checkU = str(input('Digite seu novo nome:  '))
    senha = str(input(f'Seu nome nome é "{checkU}"\npara confirmar, informe a sua senha atual: '))
    while len(senha) > 16 or len(senha) < 4:
        print('Senha Inválida.')
        senha = str(input('Senha: '))
    user = sessionName
    checkS = 'NULL'
    objAlterName = Perfil(user, senha, checkS, checkU)
    if objAlterName.perfilVerify() == True:
        objAlterName.perfilAlterName()
        objAlterName.perfilAlterHistoric()
        print('Usuário alterado com sucesso')
        sessionName = objAlterName.user
        menu()
    else:
        print('Houve algum erro.')
        menu()

def perfilSenha():
    checkS = str(input('Digite sua nova senha: '))  
    while len(checkS) > 16 or len(checkS) < 4:
        print('Senha Inválida.')
        senha = str(input('Senha: '))
    senha = str(input(f'Sua nova senha é "{checkS}"\npara confirmar. informe a sua senha atual: '))
    while len(senha) > 16 or len(senha) < 4:
        print('Senha Inválida.')
        senha = str(input('Senha: '))
    user = sessionName
    checkU = 'NULL'
    objAlterSenha = Perfil(user, senha, checkS, checkU)
    if objAlterSenha.perfilVerify() == True:
        objAlterSenha.perfilAlterSenha()
        print('Senha alterada com sucesso!')
        menu()
    else:
        print('Houve algum erro.')

def perfilHistorico():
    user = sessionName
    senha = 'NULL'
    checkS = 'NULL'
    checkU = 'NULL'
    objHistorico = Perfil(user, senha, checkS, checkU)
    objHistorico.perfilHistoric()
    menu()
start()
