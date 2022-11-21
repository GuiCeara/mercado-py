import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mercado"
)
mycursor = mydb.cursor()

class ListaProdutos():

    def catalogo():
        mycursor.execute("SELECT * FROM produtos")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(f'ID: {x[0]}\n' f'Produto: {x[1]}\n' f'Valor: R${x[3]}\n' f'Quantidade: {x[2]}\n')
        return True
