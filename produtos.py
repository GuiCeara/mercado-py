import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mercado"
)
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()

class Produtos():

    id:int = 0
    user:str = ''
    nomeProduto:str = ''
    valorProduto:float = 0.00
    quantidade:int = 0
    total:float = 0.00
    newQuant:int = 0
    esc:str = ''

    def __init__(self, id, quantidade, user) -> None:

        self.id = id 
        self.quantidade = quantidade
        self.user = user

    def verifyProdutos(self):

        mycursor.execute("SELECT * FROM produtos")

        myresult = mycursor.fetchall()
            
        for produto in myresult:
            if self.id == produto[0] and self.quantidade <= produto[2]:
                self.total = self.quantidade * produto[3]
                self.newQuant = produto[2] - self.quantidade
                self.nomeProduto = produto[1]
                self.valorProduto = produto[3]
                return True
            else:
                pass

    def confirmProdutos(self):

        sql = f"UPDATE produtos SET estoque = '{self.newQuant}' WHERE id = '{self.id}'"
        mycursor.execute(sql)
        mydb.commit()
        return True

    def addHistoric(self):
        date = datetime.datetime.now()
        sql = "INSERT INTO historico(pedidoN, fk_usuarios_usuario, nomeProduto, quantidadeTotal, precoTotal, dataCompra) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (0, self.user, self.nomeProduto, self.quantidade,  self.total, date)
        mycursor.execute(sql, val)
        mydb.commit()
