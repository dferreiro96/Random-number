''' adivinar numero y mostrar en lista refactorizado '''

import random

#definiendo funciones
def pedir_numero (mensaje):
    while True:
        try:
            num= int(input(mensaje))
        except ValueError:
            print("\nSolo se permiten números.")
            continue
        break
    return num
def pedir_opcion (mensaje, opciones):
    while True:
        try: 
            respuesta= int(input(mensaje))
            if respuesta in opciones:
                return respuesta
            else:
                print("Opción inválida")
        except ValueError:
            print("Solo números")
          
def jugar():
    lista=[]
    print()
    while True:
        contador=0
        lim_inf= pedir_numero("\nIntroduzca el primer número: ")
        lim_sup= pedir_numero("\nIntroduzca el segundo número: ")

        while lim_inf>lim_sup or lim_inf== lim_sup:
            print("""\nEl límite inferior no puede ser ni mayor ni igual que el límite superior.\n""")
            lim_inf= pedir_numero("\nIntroduzca el primer número: ")
            lim_sup= pedir_numero("\nIntroduzca el segundo número: ")
        aleat= random.randint(lim_inf, lim_sup)
        
        num=pedir_numero(f"\nBien, ahora introduzca un número entre {lim_inf} y {lim_sup}: ")

        while num!= aleat:
            contador += 1
            lista.append(num)
            if num > aleat:
                num= pedir_numero("\nEl numero es MENOR. Introduzca otro: ")
            else:
                num=pedir_numero("\nEl numero es MAYOR. Introduzca otro: ")
                
        contador +=1	
        lista.append(num)				
        print(f"\nFELICIDADES. El número es {aleat}. Lo logró en {contador} intentos.") 
        print(f"\n Los números introducidos fueron: \n{lista}")
        break  
def main():
    while True:
        
        print("\n1. Jugar.")
        print("2. Salir.")  
        if pedir_opcion("\nQué desea realizar?: ", [1, 2]) == 1:
            jugar()
        
        else:
            break

print("Este juego consiste en lo siguiente: \n\tSe le pedirán dos números entre los cuales usted quiere que el programa genere un número aleatorio. Luego, usted \ntratará de adivinar el número generado por el programa.")
#llamando al programa principal            
main()


print()
print("\nHasta luego")
