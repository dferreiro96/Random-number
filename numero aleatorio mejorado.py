''' adivinar numero y mostrar en lista'''

import random
lista=[]
print("""Este juego consiste en lo siguiente:
	 \n\tSe le pedirán dos números entre los cuales usted quiere que el programa genere un número aleatorio. Luego, usted tratará de adivinar el número generado por
el programa.""")
print()
while True:
	contador=0
	while True:
		try:
			lim_inf =int(input("\nIntroduzca el primer número: "))
		except ValueError:
			print("\n Debe introducir un número")
			continue
		break
	while True:
		try:
			lim_sup= int(input("Introduzca el segundo número: "))
		except ValueError:
			print("\nDebe introducir un número")
			continue
		break


	while lim_inf>lim_sup or lim_inf== lim_sup:
		print("""\nEl límite inferior no puede ser ni mayor ni igual que el límite superior.\n""")
		while True:
			try:
				lim_inf =int(input("Introduzca el primer número: "))
			except ValueError:
				print("Debe introducir un número")
				continue
			break
		while True:
			try:
				lim_sup= int(input("Introduzca el segundo número: "))
			except ValueError:
				print("Debe introducir un número")
				continue
			break

	aleat= random.randint(lim_inf, lim_sup)

	
	while True:
		try:
			num=int(input(f"\nBien, ahora introduzca un número entre {lim_inf} y {lim_sup}: "))
		
		except ValueError:
			print("Debe introducir un número. ")
			continue
		break
	
	
	
	while num!= aleat:
			contador += 1
			lista.append(num)
			if num > aleat:
				while True:
					try:
						num= int(input ("\nEl numero es MENOR. Introduzca otro: "))
					except ValueError:
						print("Debe introducir un numero.")
						continue
					break
			else:
				while True:
					try:
						num=int(input ("\nEl numero es MAYOR. Introduzca otro: "))
					except ValueError:
						print("Debe introducir un número")
						continue
					break
	
	contador +=1	
	lista.append(num)				
	print(f"\nFELICIDADES. El número es {aleat}. Lo logró en {contador} intentos.")

		
	salir= input("\n¿Desea jugar de nuevo? (s/n) ") .lower() .strip()
	while salir != "s" and salir != "n":
		salir= input("\nIntroduzca 's' para jugar nuevamente o 'n' para salir del programa: ") .lower() .strip()
		break		
	if salir != "s":
		print(f"""\n Los números introducidos en toda la sesión fueron: 
		\n{lista}""")
		print()
		print("\nHasta luego")
		break
	
	
	