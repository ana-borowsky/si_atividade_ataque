import json
import random
import hashlib
import itertools
import string
import time

def take_last_four_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    last_four_users = list(users.items())[-4:]

    return [info['password'] for _, info in last_four_users]

def code_cracker_3000():
        quantity = users_quantity()
        if quantity < 4:
            print("\nCadastre ao menos 4 usuários no sistema!")
        else:
            print('\nEste é o CodeCracker3000!\n')
            print('\nO programa realizará a quebra das senhas dos últimos 4 usuários cadastrados no programa.')
            print('\nIniciando a quebra de senhas...')
            hashes_to_break = take_last_four_users()
            for hash in hashes_to_break:
                start_time = time.time()
                # print(hash)
                result = brute_force_md5(hash, max_length = 3)
                end_time = time.time()
                total_time = end_time - start_time
                print("Resultado para um usuário: ", result)
            print(f'Tempo de execução: {total_time:.2f} segundos')

def users_quantity():
    with open('users.json', 'r') as file:
        users = json.load(file)

    users_quantity = len(users)
    return users_quantity

def password_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def brute_force_md5(target_password, max_length = 3):
    chars = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat = length):
            attempt = ''.join(attempt)
            # print(attempt)
            if password_hash(attempt) == target_password:
                return f'Senha encontrada: {attempt}'

    return 'Senha não encontrada'

def generateUniqueId(existingIds):
    while True:
        newId = str(random.randint(1000, 9999))
        if newId not in existingIds:
            return newId

def createUser(name, username, password):
    userData = {
        "name": name,
        "username": username,
        "password": password_hash(password),
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

    hashedPassword = hashlib.md5(password.encode()).hexdigest()
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
                print("Faça seu cadastro\n")

                name = input("Insira seu nome: ")
                username = input("Insira seu nome de usuário: ")
                password = input("Insira sua senha: ")

                createUser(name, username, password)
                print(f"\nUsuário cadastrado com sucesso!")

            case '2':
                print("\nFaça seu login\n")
                username = input("Insira seu nome de usuário: ")
                password = input("Insira sua senha: ")

                user = authenticateUser(username, password)

                if user:
                    print(f"\nLogin bem-sucedido! Boas vindas, {user['name']}!\n")
                else:
                    print("\nNome de usuário ou senha incorretos!")

            case '3':
                code_cracker_3000()

            case '4':
                print("\nMuito obrigada por usar o programa. Até mais!\n\n")
                break

            case _:
                print("\nOpção inválida!")

main()


