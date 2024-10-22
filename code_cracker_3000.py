import itertools
import string
import hashlib
import bcrypt

#sem salt
def password_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

#com salt
def password_hash_salt(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def password_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# Algoritmo da quebra do MD5
def case_cracker_3000(target_password, max_length = 4):
    chars = string.ascii_lowercase + string.digits + "#$%&@*!?,.;:()*+=-_[]{}çâãàáâúóôõéêç"

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat = length):
            attempt = ''.join(attempt)
            if password_hash(attempt) == target_password:
                return f'Senha encontrada: {attempt}'

    return 'Senha não encontrada'