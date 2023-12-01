import mysql.connector
import tkinter as tk
from tkinter import messagebox

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '123456',
        database = 'teste'
    )
except mysql.connector.Error as erro:
    print(f'Erro de conexão: {erro}')
    

cursor = conexao.cursor()

def inserir_dados():
    try:
        nome = txt_nome.get()
        comando = f'INSERT INTO pessoa(nome_pessoa) VALUES("{nome}");'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('Info', 'Dado inserido com sucesso')
    except mysql.connector.Error as erro:
        messagebox.showerror('Erro', f'Erro {erro}')




def mostrar_dados():
    comando=f'SELECT * FROM pessoa;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

def atualiza_dados():
    try:
        nome = txt_nome.get()
        valor = txt_id.get()
        comando = f'UPDATE pessoa SET nome_pessoa = "{nome}"  WHERE id_pessoa = {valor};'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('Info', 'Atualizado com sucesso')
    except mysql.connector.Error as erro:
        print('Erro', f'Erro {erro}')


def deletar_dados():
    valor = txt_id.get()
    comando= f'DELETE FROM pessoa WHERE id_pessoa = {valor}'
    cursor.execute(comando)
    conexao.commit()


janela = tk.Tk()
janela.title('Tela de teste')
janela.geometry('400x400')

lbl_id = tk.Label(janela, text='Id:')
lbl_id.place(x=10, y=10)

txt_id = tk.Entry(janela)
txt_id.place(x=10, y=30)

lbl_nome = tk.Label(janela, text='Nome: ')
lbl_nome.place(x=10, y=50)

txt_nome = tk.Entry(janela)
txt_nome.place(x=10, y=70)

btn_enviar = tk.Button(janela, text='Enviar', command=inserir_dados)
btn_enviar. place(x=10, y=100)

btn_mostar = tk.Button(janela, text='Mostar', command=mostrar_dados)
btn_mostar.place(x=10, y=130)

btn_atualizar = tk.Button(janela, text='Atualizar', command=atualiza_dados)
btn_atualizar.place(x=10, y=160)

btn_deletar = tk.Button(janela, text='Deletar', command=deletar_dados)
btn_deletar.place(x=10, y=190)

janela.mainloop()