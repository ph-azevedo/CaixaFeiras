import sqlite3, os
## 9788543102818
con = sqlite3.connect('db.db')
cur = con.cursor()

import keyboard, time

def menu():
    print('O que deseja fazer?')
    print('''
    1. Consulta\n
    2. Venda''')

    while True:
        if keyboard.is_pressed('1'):
            cls()
            consulta()
            break
        elif keyboard.is_pressed('2'):
            Venda()
            cls()

def consulta():
    con2 = sqlite3.connect('db.db')
    cur2 = con2.cursor()
    erase()
    isbn = input('Leia o código de barras\n')
    query = cur2.execute(f'SELECT descricao, valor FROM estoque where isbn={isbn}')
    result = query.fetchone()
    cls()
    print(f'Título: {result[0]}\nPreço: R$ {result[1]}')
    cur2.close()
    con2.close()
    time.sleep(3)
    cls()
    menu()


class Venda:
    total = 0.00
    def __init__(self):
        cur.execute(f'INSERT INTO VENDA(total) VALUES(0.00)')
        self.vendaid = cur.lastrowid
        self.menu_venda()

    def menu_venda(self):
        print(self.vendaid)
        erase()
        print()
        print('Produtos no pedido:')
        self.lista_prods()
        print()
        print('''
        1. Adicionar Produto\n
        2. ----------\n
        3. Finalizar venda\n
        4. Cancelar venda
        ''')
        while True:
            if keyboard.is_pressed('1'):
                cls()
                self.add_prod()
                break

            elif keyboard.is_pressed('3'):
                cls()
                self.finaliza_venda()
                break

            elif keyboard.is_pressed('4'):
                cls()
                erase()
                opt = int(input('Deseja realmente cancelar? Digite 1 para sim ou 2 para não: '))
                if opt == 1:
                    menu()
                else:
                    self.menu_venda()
                break

    def add_prod(self):
        erase()
        prod = input('Leia o código de barras\n')
        quant = input('Digite a quantidade:\n')
        item = cur.execute(f'SELECT ISBN, VALOR FROM ESTOQUE WHERE ISBN={prod}')
        result = item.fetchall()[0]
        total = float(result[1]) * float(quant)
        cur.execute(f'INSERT INTO ITEMVENDA(ISBN, QUANTIDADE, VALOR, TOTAL, VENDA) VALUES({result[0]}, {quant}, {result[1]}, {total}, {self.vendaid})')
        cls()
        self.menu_venda()

    def lista_prods(self):
        total = 0.00
        lista = cur.execute(f'SELECT ISBN, QUANTIDADE FROM ITEMVENDA WHERE VENDA={self.vendaid}')
        result = lista.fetchall()
        if len(result) != 0:
            for item in result:
                query = cur.execute(f'SELECT ISBN, DESCRICAO, VALOR FROM ESTOQUE WHERE ISBN={item[0]}')
                result = query.fetchall()
                total = (float(result[0][2]) * float(item[1])) + total
                print(f'{result} - Qtde: {item[1]}')
            print(f'Total: R$ {total}')
            self.total = total

    def finaliza_venda(self):
        cur.execute(f'INSERT INTO VENDA(total) VALUES({self.total})')
        print('''Qual a forma de pagamento?\n\n
                1. Dinheiro\n
                2. Cartão\n
                
                ''')
        while True:
            if keyboard.is_pressed('1'):
                cls()
                print(f'Total: R$ {self.total}')
                erase()
                erase()
                recebido = float(input('Valor recebido:'))
                troco = recebido - self.total
                print(f'Troco: R$ {troco}')
                input('Pressione enter para sair')
                break

            elif keyboard.is_pressed('2'):
                cls()
                print(f'Total: R$ {self.total}')
                erase()
                erase()
                input('Pressione enter para sair')
                break
        con.commit()
        print('Venda registrada!')
        time.sleep(3)
        menu()
def cls():
    os.system('cls')


def erase():
    keyboard.press_and_release('backspace')

menu()