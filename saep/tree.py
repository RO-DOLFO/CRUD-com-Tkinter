import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Conectar ao banco de dados
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='teste'
    )
except mysql.connector.Error as erro:
    print(f'Erro de conexão: {erro}')

cursor = conexao.cursor()

def carregar_dados():
    try:
        # Limpa os itens existentes no TreeView
        tree.delete(*tree.get_children())

        # Consulta os dados da tabela pessoa
        cursor.execute('SELECT * FROM pessoa;')
        resultado = cursor.fetchall()

        # Insere os dados no TreeView
        for row in resultado:
            tree.insert('', 'end', values=row)
            
    except mysql.connector.Error as erro:
        messagebox.showerror('Erro', f'Erro {erro}')

def adicionar_item():
    try:
        nome = entry_nome.get()
        comando = f'INSERT INTO pessoa(nome_pessoa) VALUES("{nome}");'
        cursor.execute(comando)
        conexao.commit()
        messagebox.showinfo('Info', 'Dado inserido com sucesso')
        carregar_dados()
    except mysql.connector.Error as erro:
        messagebox.showerror('Erro', f'Erro {erro}')

# Cria a janela principal
janela = tk.Tk()
janela.title('Tela de teste')
janela.geometry('400x400')

# Cria um Treeview
tree = ttk.Treeview(janela, columns=("ID", "Nome"))
tree.column("#0", width=100, minwidth=100)
tree.column("ID", width=100, minwidth=100)
tree.column("Nome", width=100, minwidth=100)

tree.heading("#0", text="ID", anchor=tk.W)
tree.heading("ID", text="ID", anchor=tk.W)
tree.heading("Nome", text="Nome", anchor=tk.W)

# Adiciona um botão para recarregar os dados no TreeView
btn_recarregar = tk.Button(janela, text='Recarregar Dados', command=carregar_dados)
btn_recarregar.pack(pady=10)

# Adiciona um botão e entradas para adicionar itens à árvore
lbl_nome = tk.Label(janela, text='Nome:')
entry_nome = tk.Entry(janela, width=15)
btn_adicionar = tk.Button(janela, text='Adicionar Item', command=adicionar_item)

# Rótulos e posicionamento na janela
lbl_nome.pack(pady=5)
entry_nome.pack(pady=5)
btn_adicionar.pack(pady=5)

# Posiciona o Treeview na janela
tree.pack(pady=10)

# Inicializa o TreeView com dados da tabela pessoa
carregar_dados()

# Inicia o loop principal
janela.mainloop()
