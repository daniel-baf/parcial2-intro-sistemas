try: 
	print("ingrese un valor: ", end="")
	entry_1 = int(input())

	# comparamos valores
	is_odd = entry_1 % 2 == 0

	print("es par: ", end="")
	print(is_odd)
except:
	print("error ejecutando el programa")
