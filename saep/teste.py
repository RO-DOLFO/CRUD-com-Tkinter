nome = "rodolfo"
valor= 1

comando = f'UPDATE pessoa SET nome_pessoa = "{nome}"  WHERE id_pessoa = {valor};'
print(comando)
