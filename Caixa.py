import sqlite3, os
## 9788543102818
con = sqlite3.connect('db.db')
cur = con.cursor()

import keyboard  # using module keyboard

def menu():
    print('O que deseja fazer?')
    print('''
    1. Consulta\n
    2. Venda''')

    while True:
        if keyboard.is_pressed('1'):  # if key 'q' is pressed
            os.system('cls')
            consulta()
            break
def consulta():
    isbn = input('Leia o código de barras\n')
    query = cur.execute(f'SELECT descricao FROM estoque where isbn={isbn}')
    cls()
    print(query.fetchone())


def cls():
    os.system('cls')


menu()