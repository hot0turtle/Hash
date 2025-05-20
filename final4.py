#Trabalho Leonardo Siqueira Hanke
import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = []
usernames = []
def load_users():
    global users
    users.clear()
    with open("credenciais.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users.append(User(username, password))


def criarUser():
    username = input("Digite o nome de usuário: ")[:4]
    
    if username not in nome_check():
        
        password = input("Digite a senha: ")[:4]
        password_hash = hashlib.md5(password.encode()).hexdigest()
        with open("credenciais.txt", "a") as file:
            file.write(f"{username},{password_hash}\n")
    
        load_users()
        print(f"Usuário '{username}' criado com sucesso.\n")
        menu()
    else:
        print("esse username ja esta sendo utilizado\n")
        menu()


def autentica():

    get_name = input("Qual o seu User?")[:4]
    for user in users:
        if get_name == user.username:
            get_pass = input("Qual a senha?")[:4]
            get_pass_hash = hashlib.md5(get_pass.encode()).hexdigest()
            if get_pass_hash == user.password:
                print("\nautenticado\n")
                menu()
                break
            else:
                print("\nfalha na autenticação\n")
                menu()
                break
    else:
        print("Usuário não encontrado.\n")
        menu()
        

def menu():
    opcao = input("1 - Autenticar\n2 - Cadastrar novo User\n3 - Sair\nEscolha uma opção: ")

    if opcao == "1":
        autentica()
    elif opcao == "2":
        criarUser()
    elif opcao == "3":
        print("Saindo...")
    else:
        print("Opção inválida. Encerrando.")

def nome_check():
    for user in users:
        usernames.append(user.username)
    return(usernames)


if __name__ == "__main__":
    load_users()
    menu()