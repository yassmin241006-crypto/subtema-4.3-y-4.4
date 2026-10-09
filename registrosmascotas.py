import os
nombre_mascotas=[""]*3 #pupi
edad_mascotas=[0]*3  #3
def insertar():
    for i in range(len(nombre_mascotas)): #.Length en c#
        nombre_mascotas[i]=input(f"ingrese nombre de la mascota: ")
        edad_mascotas[i]=input(f"ingrese edad mascota: ")

def mostrar():
    for i in range(len(nombre_mascotas)): #.Length en c#
      print(f"nombre: {nombre_mascotas[i]},edad: {edad_mascotas[i]}")
    input("presione para continuar")

def main():
   global nombre_mascotas, edad_mascotas #para modificar las listas declaradas fuera del arreglo
   #arreglos paralelos ambas listas deben tener la misma longitud
   nombre_mascotas=[""]*3 #iniciar la lista vacia para cadenas de longitud 3
   edad_mascotas=[0]*3 #iniciar la lista vacia para numeros enteros de longitud 3

   opcion=0
   while opcion !=4: ##opcion distinto a 4 (true)
    os.system('cls' if os.name== 'nt' else 'clear') #limpiar la consola
    print ("[1] Insertar mascota (nombre|edad)")
    print ("[2] Mostrar mascota (nombre|edad)")
    print ("[3] Eliminar mascota por nombre (en ambos vesctores)")
    print ("[4] Salir")
    opcion = int(input("elije una opcion: "))
    if opcion ==1:
     insertar()
    elif opcion==2:
     print("mostrar")
    elif opcion==3:
     print("eliminar")  
    elif opcion==4:
     print ("saliendo...")
    else: print("opcion invalida")
    if opcion !=4: input("presioe para continuar..") #espere a la interaccion del usuario para recargar el manu
main()
     