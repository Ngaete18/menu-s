nombre = ""
edad = 0
correo = ""
opc = 0

while True:
  print('''
  ---MENU---
  1)Agregar Nombre
  2) Agregar Edad
  3)Agregar Correo
  4)Mostrar
  5)Salir
  ''')

  opc = input("Opcion: ")

  if not opc.isnumeric():
    print("Opcion no valida ingrese de nuevo")
    opc = input("Opcion: ")

  opc = int(opc)

  if opc == 1:
    nombre = input()

  elif opc == 2:
    edad = int(input())

  elif opc == 3:
    correo = input()

  elif opc == 4:
    print("nombre: ", nombre)
    print("edad: ", edad)
    print("correo: ", correo)

  elif opc == 5:
    print("gracias por tu tiempo :) ")
    break