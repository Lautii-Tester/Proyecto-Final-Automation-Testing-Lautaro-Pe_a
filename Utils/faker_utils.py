from faker import Faker

fake = Faker()

def generar_usuario(num_usuarios=5):
    usuarios = []
    usuario_valido = "standard_user"
    password_valida = "secret_sauce"

    for _ in range(num_usuarios):
        
        if fake.boolean(chance_of_getting_true=30): # 30% de probabilidad de generar un usuario válido
            username = usuario_valido
            password = password_valida
            login_esperado = True

        else:
            username = fake.user_name()
            password = fake.password()
            login_esperado = False

        usuarios.append((username, password, login_esperado))

    return usuarios