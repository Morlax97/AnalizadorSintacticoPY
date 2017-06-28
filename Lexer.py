#string="insertar string de prueba acá"


string+=" "
i=0
k=0
pretoken=""
tokens=[]
cIgualParentesis=0

while True:
	if i<len(string):
		if string[i]=='"':
			#Armando el auxiliar con cada token
			while string[i+k]!='"':
				if i+k==len(string):
					print("ERROR: FALTA CERRAR EL STRING")
					break
				pretoken+=string[i+k]
				k+=1
			if string[i+k+1] not in [" ", "(", ")", "="]:
				print("ERROR: CARACTERES LUEGO DEL STRING")
				#Por ejemplo "asdasd"as ^
				break
			else:
				tokens.append("<STRING>")
		#Chequeo de palabra/s
		elif string[i].isalpha():
			while string[i+k].isalpha():
				pretoken+=string[i+k]
				k+=1
			if string[i+k] not in [" ", "(", ")", "=", ">", "<"]:
				print("ERROR: COMBINACIÓN DE ALFANUMÉRICOS")
				break
			else:
				#Palabras Reservadas
				if pretoken in ["and", "or", "not"]:
					tokens.append("<OPLOG>")
				elif pretoken in ["true", "false"]:
					tokens.append("<BOOL>")
				elif pretoken=="define":
					tokens.append("<DEFINE>")
				elif pretoken=="if":
					tokens.append("<IF>")
				elif pretoken=="set":
					tokens.append("<SET>")
				#Identificador
				else:
					tokens.append("<ID>")
		#Chequeo de números	
		elif string[i].isdigit():
			while string[i+k].isdigit():
				pretoken+=string[i+k]
				k+=1
			if string[i+k] not in [" ", "(", ")", "=", ">", "<", "+", "*", "^"]:
				print("ERROR: COMBINACIÓN DE ALFANUMÉRICOS")
				break
			else:
				tokens.append("<NUM>")
		#Operadores de Relación
		elif string[i] in ["<", ">", "="]:
			if string[i+1]=="=":
				k=2
			else:
				k=1
			tokens.append("<OPREL>")
		#Operadores Matemáticos
		elif string[i] in ["+", "*", "^"]:
			k=1
			tokens.append("<OPMAT>")
		#Paréntesis abierto
		elif string[i]=="(":
			k=1
			cIgualParentesis+=1
			tokens.append("<(>")
		#Paréntesis cerrado con chequeo
		elif string[i]==")":
			if cIgualParentesis<1:
				print("ERROR: DISCREPANCIA ENTRE PARÉNTESIS ABIERTOS Y CERRADOS")
				break
			else:
				k=1
				cIgualParentesis-=1
				tokens.append("<)>")
			
		elif string[i]!=" ":
			print("ERROR: CARACTERES NO RECONOCIDOS POR EL LENGUAJE")
			break
		else:
			k=1

		i+=k
		k=0
		pretoken=""

	else:
		print(tokens)
		break

