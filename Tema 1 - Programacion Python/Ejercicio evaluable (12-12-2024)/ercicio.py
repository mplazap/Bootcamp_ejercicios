#Importaciones para fecha e ID aleatorio de usuario
from datetime import datetime
import random

class Usuarios:
    def __init__(self, nombre, apellido, dni, altura, email, estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.altura = float(altura)
        self.edad = None  # La edad se inicializa en "None"
        self.email = email
        self.estudiante = estudiante
        self.id = random.randint(0, 999)  # Se genera un "ID" único

    # Método para calcular la edad
    def calcular_edad(self):
        nacimiento = input(f"Dime tu año de nacimiento de {self.nombre}: ")
        now = datetime.now()
        self.edad = now.year - int(nacimiento)

    # Para mostrar datos del usuario por pantalla
    def __str__(self):
        return (f"Usuarios:\n Nombre = {self.nombre}\n Apellido = {self.apellido}\n"
                f" DNI = {self.dni}\n Altura = {self.altura}m\n Edad = {self.edad if self.edad else 'Desconocida'} años\n"
                f" Email = {self.email}\n Estudiante = {'Sí' if self.estudiante else 'No'}\n ID = {self.id}\n")


# Año actual
hoy = datetime.now().year

# Usuarios de ejemplo ya añadidos
usuario1 = Usuarios(nombre="Pepe", apellido="Martinez", dni="8907654Y", altura=1.75, email="usuario1@gmail.com", estudiante=True)
usuario1.edad = hoy - 2012

usuario2 = Usuarios(nombre="Luis", apellido="Gonzalez", dni="6923837Q", altura=1.90, email="usuario2@gmail.com", estudiante=False)
usuario2.edad = hoy - 1979

usuario3 = Usuarios(nombre="Juan", apellido="Lopez", dni="2840281P", altura=1.68, email="usuario3@gmail.com", estudiante=True)
usuario3.edad = hoy - 2000

usuarios = [usuario1, usuario2, usuario3]

# Menú
menu = """
Bienvenido, elije una de las opciones:\n
    1.- Ver todos los usuarios
    2.- Ordenar usuarios por edad descendente
    3.- Buscar usuario por Email
    4.- Crear nuevo usuario
    5.- Actualizar usuario existente
    6.- Borrar usuario
    7.- Borrar todos los usuarios
    8.- Salir
"""

while True:
    opcion = int(input(menu))
    if 1 <= opcion <= 8:
        match opcion:
            case 1:
                # Mostrar todos los usuarios
                if usuarios:
                    for usuario in usuarios:
                        print(usuario)
                else:
                    print("No hay usuarios registrados.")
            case 2:
                # Ordenar usuarios por edad descendente
                usu_orden_descen = sorted(usuarios, key=lambda o: o.edad if o.edad is not None else -1, reverse=True)
                for usuario in usu_orden_descen:
                    print(usuario)
                    
            case 3:
                # Buscar usuario por Email
                correo = input("Correo del usuario a buscar: ")
                usuario_encontrado = next((u for u in usuarios if u.email.lower() == correo.lower()), None)
                if usuario_encontrado:
                    print(usuario_encontrado)
                else:
                    print("Usuario no encontrado.")
                    
            case 4:
                # Crear un nuevo usuario
                nombre = input("Introduce el nombre de usuario: ")
                apellido = input("Introduce el apellido de usuario: ")
                altura = float(input("Introduce la altura del usuario (en metros): "))
                dni = input("Introduce el DNI de usuario: ")
                email = input("Introduce el Email de usuario: ")

                # Control de la respuesta de si eres estudiante 
                while True:
                    respuesta = input("¿Es estudiante? (sí/no): ").strip().lower()
                    if respuesta in ("sí", "si", "s", "yes", "y"):
                        estudiante = True
                        break
                    elif respuesta in ("no", "n"):
                        estudiante = False
                        break
                    else:
                        print("Por favor, responde con 'sí' o 'no'.")

                nuevo_usuario = Usuarios(nombre, apellido, dni, altura, email, estudiante)
                nuevo_usuario.calcular_edad()  # Calcula la edad del usuario
                usuarios.append(nuevo_usuario)
                print("El usuario se ha creado satisfactoriamente.")
                
            case 5:
                # Actualizar usuario existente
                correo = input("Introduce el email del usuario a actualizar: ")
                usuario_encontrado = next((u for u in usuarios if u.email.lower() == correo.lower()), None)
                if usuario_encontrado:
                    usuario_encontrado.nombre = input("Nuevo nombre: ")
                    usuario_encontrado.apellido = input("Nuevo apellido: ")
                    usuario_encontrado.dni = input("Nuevo DNI: ")
                    usuario_encontrado.altura = float(input("Nueva altura (en metros): "))
                    usuario_encontrado.email = input("Nuevo email: ")
                    usuario_encontrado.estudiante = input("¿Es estudiante? (sí/no): ").strip().lower() == "sí"
                    print("Usuario actualizado.")
                else:
                    print("Usuario no encontrado.")
                    
            case 6:
                # Borrar un usuario
                correo = input("Introduce el email del usuario a borrar: ")
                usuarios = [u for u in usuarios if u.email.lower() != correo.lower()]
                print("Usuario borrado.")
                
            case 7:
                # Borrar todos los usuarios
                usuarios.clear()
                print("Todos los usuarios han sido borrados.")
                
            case 8:
                # Salir del programa1
                print("¡Hasta pronto!")
                break
    
    # Si se elige una opcion incorrecta
    else:
        print("No has elegido una opción correcta.")
