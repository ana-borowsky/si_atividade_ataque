import json
import random
import hashlib

def generateUniqueId(existingIds):
    while True:
        newId = str(random.randint(1000, 9999))
        if newId not in existingIds:
            return newId

def createUser(name, username, password):
    userData = {
        "name": name,
        "username": username,
        "password": hashlib.md5(password.encode()).hexdigest(),
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
        - [ 3 ] Sair \n\n \
        > Sua opção: ")

        if userOption == "1":
            print("Faça seu cadastro\n")

            name = input("Insira seu nome: ")
            username = input("Insira seu nome de usuário: ")
            password = input("Insira sua senha: ")

            createUser(name, username, password)
            print(f"\nUsuário cadastrado com sucesso!")

        elif userOption == "2":
            print("\nFaça seu login\n")
            username = input("Insira seu nome de usuário: ")
            password = input("Insira sua senha: ")

            user = authenticateUser(username, password)

            if user:
                print(f"\nLogin bem-sucedido! Boas vindas, {user['name']}!\n")
            else:
                print("\nNome de usuário ou senha incorretos!")

        elif userOption == "3":
            print("\nMuito obrigada por usar o programa. Até mais!\n\n")
            break

        else:
            print("\nOpção inválida!")

main()
