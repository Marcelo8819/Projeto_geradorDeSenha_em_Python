import random  # serve para importar um número aleatório 
import string  # é a biblioteca com opções de senhas disponiveis 

def password_generator(len_pass = 8):   # def serve para definir o nome da funçaõ em python 
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options 

    password_user = ""

    for i in range(0, len_pass):   # o range cria uma array de 0 até o número digitado no len_pass
            digit =  random.choice(options)  
            password_user = password_user + digit


    return password_user

choice_user = input("Quantos digitos na senha? ")

if choice_user.isdigit():       # esta é uma verificação pra saber se realmente usuário digitou a senha com o tipo correto
        choice_user = int(choice_user)
else:
        print("Entrada inválida!")
        quit()

response =  password_generator(len_pass = choice_user)
print(f"Senha gerada: \n{response}")


