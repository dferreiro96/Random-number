"""
el numero oculto
"""
import random
historial= []
print("Este es un jueo dende se enumera un número aleatorio y UD deberá intentar adivinarlo. ")
print("Entre qué números quiere que se encuentre el numero aleatorio?")
limite_inferior= int(input(( "Límite inferior: ")))
limite_superior= int(input(("Límite superior: ")))
while limite_superior<= limite_inferior:
    print("El límite superior no puede ser menor ni iual que el límite inferior")
    limite_inferior= int(input(( "Límite inferior: ")))
    limite_superior= int(input(("Límite superior: ")))
    
aleatorio= random.randint(limite_inferior,limite_superior)

intentos= 0
num= int(input(f"Se ha enerado un número aleatorio entre {limite_inferior} y {limite_superior}. Intente adiinarlo: \n"))

while True:
 intentos +=1
 if num  < limite_inferior or num > limite_superior:
     num= int(input(("Introdujo un número fuera del rano. Intente nueamente:")))
     continue
 elif limite_inferior> limite_superior:
     num= int(input(("El límite inferior no puede ser mayor que el límite superior. Intente nueamente:")))
     continue


 if num < aleatorio:
       num=int(input(("El nùmero que ud introdujo es menor. Intente nueamente: ")))
 elif aleatorio < num:
       num= int(input(("El nùmero que ud introdujo es mayor. Intente nueamente: ")))

 else:
       print(f"FELICIDADES!! Lo ha alcanzado en {intentos} intentos.") 
       
       partida={
           "Intentos": intentos, 
           "Número": aleatorio,
           "Rano": {f"limite_inferior - limite_superior"}
       }
       historial.append(partida)
       
       print("\n--- HISTORIAL ---")
       for i, p in enumerate(historial, 1):
            print(f"Partida {i}: Número {p['Número']} en {p['Intentos']} intentos (rango {p['Rano']})")
            print("¡Gracias por jugar!")
       break
