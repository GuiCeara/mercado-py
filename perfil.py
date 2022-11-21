import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mercado"
)
mycursor = mydb.cursor()

class Perfil():

    user:str = ''
    senha:str = ''
    userResult: str = ''
    checkS:str = ''
    checkU:str = ''

    def __init__(self, user, senha, checkS, checkU) -> None:
        self.user = user
        self.senha = senha
        self.checkS = checkS
        self.checkU = checkU
    
    def perfilVerify(self):
        mycursor.execute("SELECT * FROM usuarios")
        myresult = mycursor.fetchall()
        for obj in myresult:
            if self.user == obj[0] and self.senha == obj[1]:
                self.userResult = obj[0]
                return True
            else:
                pass
    
    def perfilAlterName(self):
        self.user = self.checkU
        sql = f"UPDATE usuarios SET usuario = '{self.user}' WHERE usuario = '{self.userResult}'"
        mycursor.execute(sql)
        mydb.commit()
    
    def perfilAlterSenha(self):
        sql = f"UPDATE usuarios SET senha = '{self.checkS}' WHERE usuario = '{self.userResult}'"
        mycursor.execute(sql)
        mydb.commit()

    def perfilAlterHistoric(self):
        self.user = self.checkU
        sql = f"UPDATE historico SET fk_usuarios_usuario ='{self.user}' WHERE fk_usuarios_usuario = '{self.userResult}' "
        mycursor.execute(sql)
        mydb.commit()

    def perfilHistoric(self):
        mycursor.execute(f"SELECT pedidoN, nomeProduto, quantidadeTotal, precoTotal, dataCompra FROM historico WHERE fk_usuarios_usuario = '{self.user}' ")
        myresult = mycursor.fetchall()
        for dado in myresult:
            print(f'\nPedido Nº: {dado[0]}\nNome do produto: {dado[1]}\nQuantidade do produto: {dado[2]}\nPreço do pedido: {dado[3]}\nData da Compra: {dado[4]}')
        
        
            

    