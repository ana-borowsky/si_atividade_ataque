import json
import random
import time
from code_cracker_3000 import case_cracker_3000, password_hash, password_hash_salt

# sem usar salt
def register_user_menu():
    print("Faça seu cadastro\n")

    name = input("Insira seu nome: ")
    username = input("Insira seu nome de usuário: ")
    password = input("Insira sua senha: ")

    createUser(name, username, password)
    print(f"\nUsuário cadastrado com sucesso!")

def login_user_menu():
    print("\nFaça seu login\n")
    username = input("Insira seu nome de usuário: ")
    password = input("Insira sua senha: ")

    user = authenticateUser(username, password)

    if user:
        print(f"\nLogin bem-sucedido! Boas vindas, {user['name']}!\n")
    else:
        print("\nNome de usuário ou senha incorretos!")

def take_last_four_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    last_four_users = list(users.items())[-4:]

    return [info['password'] for _, info in last_four_users]

def code_cracker_3000_menu():
        quantity = users_quantity()
        if quantity < 4:
            print("\nCadastre ao menos 4 usuários no sistema!")
        else:
            print('\nEste é o CodeCracker3000!\n')
            print('\nO programa realizará a quebra das senhas dos últimos 4 usuários cadastrados no programa.')
            print('\nIniciando a quebra de senhas...')
            hashes_to_break = take_last_four_users()
            counter = 0
            for hash in hashes_to_break:
                start_time = time.time()
                result = case_cracker_3000(hash, max_length = 4)
                end_time = time.time()
                total_time = end_time - start_time
                counter += 1
                print(f"Resultado para o {counter} usuário: ", result)
            print(f'Tempo de execução: {total_time:.2f} segundos')

def users_quantity():
    with open('users.json', 'r') as file:
        users = json.load(file)

    users_quantity = len(users)
    return users_quantity

def generateUniqueId(existingIds):
    while True:
        newId = str(random.randint(1000, 9999))
        if newId not in existingIds:
            return newId

def createUser(name, username, password):
    userData = {
        "name": name,
        "username": username,
        "password": password_hash_salt(password),
    }

    with open("users.json", "r+") as file:
        usersCredentials = json.load(file)

        userId = generateUniqueId(usersCredentials.keys())
        usersCredentials[userId] = userData

        file.seek(0)
        json.dump(usersCredentials, file)

def authenticateUser(username, password):
    usersCredentials = {}
    with open("users.json", "r") as file:
        usersCredentials = json.load(file)

    hashedPassword = password_hash(password)
    for userId, userData in usersCredentials.items():
        if userData["username"] == username:
            if userData["password"] == hashedPassword:
                return userData
            else:
                with open("users.json", "w") as file:
                    usersCredentials[userId] = userData
                    json.dump(usersCredentials, file)

def main():
    print("Seja bem-vindo!")

    while True:
        userOption = input("\nEscolha a opção desejada:\n \
        - [ 1 ] Cadastro \n \
        - [ 2 ] Login\n \
        - [ 3 ] CodeCracker3000!\n \
        - [ 4 ] Sair \n\n \
        > Sua opção: ")

        match(userOption):
            case '1':
                register_user_menu()
            case '2':
                login_user_menu()
            case '3':
                code_cracker_3000_menu()
            case '4':
                print("\nMuito obrigada por usar o programa. Até mais!\n\n")
                break
            case _:
                print("\nOpção inválida!")

main()


