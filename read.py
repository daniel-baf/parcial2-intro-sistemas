try: 
	print("ingrese el primer numero: ", end="")
	entry_1 = int(input())

	print("ingrese el segundo numero: ", end="")
	entry_2 = int(input())
	
	# comparamos valores
	backup = entry_1
	if(entry_1 >= entry_2): 
		entry_1 = entry_2
		entry_2 = backup

	print("el valor mas grande es: ", end="")
	print(entry_2)
except:
	print("error ejecutando el programa")
