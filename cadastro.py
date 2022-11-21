import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mercado"
)
mycursor = mydb.cursor()

class Cadastro():

    user:str = ''
    senha:str = ''

    def __init__(self, user, senha) -> None:
        self.user = user
        self.senha = senha

    def cadastrarVerify(self):
        
        l:list = []

        mycursor.execute("SELECT * FROM usuarios")

        myresult = mycursor.fetchall()

        for i in myresult:
            l.append(i[0]) 

        if self.user in l:
            print('Usuário já registrado')
            exit()
        else:
            return True

    def cadastrarC(self):
        sql = "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)"
        val = (self.user, self.senha)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Usuário cadastrado com sucesso!")

        

