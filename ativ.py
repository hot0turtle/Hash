# Acessar: https://tinyurl.com/expcriativa1

usuario = "teste2"
senha   = "abcde"

# Abri arquivo para escrita
with open("credenciais.txt", "a") as arquivo:
    arquivo.write(f"{usuario},{senha}\n")

# Abri o arquivo para leitura e li todas as linhas
with open("credenciais.txt", "r") as arquivo:
    conteudo = arquivo.readlines()

# Para cada linha em conteúdo
for linha in conteudo:
    # Separo a linha que representa o usuário pela vírgula
    usuario = linha.split(",")

    # Armazeno o nome do usuário
    nome_usuario = usuario[0]

    # Armazeno a senha do usuário
    senha_usuario = usuario[1].replace("\n", "")

    if senha == senha_usuario:
        print("senhas iguais")

    print(nome_usuario, senha_usuario)
    
