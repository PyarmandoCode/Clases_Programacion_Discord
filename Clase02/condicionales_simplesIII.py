usuarios = {
    "usuario1":"contraseña1",
    "usuario2":"contraseña2",
    "usuario3":"contraseña3"
}


# print(usuarios["usuario3"])

usuario = input("Ingrese el Nombre del usuario:")#admin
contraseña = input("Ingrese su contraseña:")

if usuario in usuarios and usuarios[usuario] == contraseña:
    print(f"Autenticacion exitosa Bienvenido {usuario}")
else:
    print("Nombre de usuario o contraseña incorrecta")    