def lexer(string):
	string += " "
	i = 0
	k = 0
	pretoken = ""
	tokens = []
	while True:
		if i < len(string):
			#Strings
			if string[ i ] == '"':
			#Armando el auxiliar con cada token (Strings)
				while string[ i + k ] != '"':
					if i + k == len(string):
						print("ERROR: FALTA CERRAR EL STRING")
						break
					pretoken += string [ i + k ]
					k += 1
				if i + k + 1 == len(string):
					tokens.append(( "<STRING>" , pretoken ))
				elif string[ i + k + 1 ] not in [ " " , ")" ]:
					print("ERROR: CARACTERES LUEGO DEL STRING")
					break
				else:
					tokens.append(( "<STRING>" , pretoken ))
			#Chequeo de palabra/s
			elif string[ i ].isalpha():
				#Armando el auxiliar con cada token (palabras)
				while string[ i + k ].isalpha():
					pretoken += string[i+k]
					k += 1
					if i + k == len(string):
						tokens.append(( "<ID>" , pretoken ))
				if string[ i + k ] not in [ " " , ")" ]:
					print("ERROR: COMBINACION DE ALFANUMERICOS")
					break
				#Palabras Reservadas
				if pretoken in [ "or", "not" ]:
					tokens.append(("<OPLOG>" , pretoken))
				elif pretoken in [ "true" , "false" ]:
					tokens.append(( "<BOOL>" , pretoken ))
				elif pretoken == "define":
					tokens.append(( "<DEFINE>" , pretoken ))
				elif pretoken == "if":
					tokens.append(( "<IF>" , pretoken ))
				elif pretoken == "set":
					tokens.append(( "<SET>" , pretoken ))
				elif pretoken == "and":
					tokens.append(( "<AND>" , pretoken ))
				#Identificador
				else:
					tokens.append(( "<ID>" , pretoken ))
			#Chequeo de numeros	
			elif string[ i ].isdigit():
				#Armando el auxiliar con cada token (numeros)
				while string[ i + k ].isdigit():
					pretoken += string[ i + k ]
					k += 1
					if i + k == len(string):
						tokens.append(( "<NUM>", int(pretoken) ))
				if string[i+k] not in [ " " , ")" ]:
					print("ERROR: COMBINACION DE ALFANUMERICOS")
					break
				else:
					tokens.append(("<NUM>", int(pretoken)))
			#Operadores de Relacion
			elif string[i] in ["<", ">", "="]:
				if ( i + 1 ) == len(string):
					tokens.append(( "<OPREL>" , string[i] ))
				elif string[ i + 1 ] == "=":
					k = 2
					tokens.append(( "<OPREL>", string[i+1] ))
				else:
					k = 1
				tokens.append(( "<OPREL>" , string[i] ))
			#Operadores Matematicos
			elif string[i] in ["+", "*", "^"]:
				k = 1
				tokens.append(( "<OPMAT>" , string[i] ))
			#Parentesis abierto
			elif string[i] == "(":
				k = 1
				tokens.append(( "<(>" , string[i] ))
			#Parentesis cerrado
			elif string[i] == ")":
				k = 1
				tokens.append(( "<)>" , string[i] ))
			#Newlines
			elif string[i] == "\\":
				if string[ i + 1 ] == "n":
					k=2
				else:
					print("ERROR: CARACTERES NO RECONOCIDOS POR EL LENGUAJE")
					break
 			#Caracteres desconocidos
			elif string[i] != " ":
				print("ERROR: CARACTERES NO RECONOCIDOS POR EL LENGUAJE")
				break
			else:
				k = 1
			i += k
			k = 0
			pretoken = ""
		else:
			print(tokens)
			return tokens
		
lexer("(this is the rarest pepe in this document + 1 >")
lexer(") this stuff is not valid m8 ()(")
lexer(" 1 + 1 + 1 + 1 + 1 + 1 + + 1 + 1 + 1 + 1 + 1 + 1 + 1")
lexer("a > b and b >= c")
lexer("define set let memes go ")
lexer ('')
lexer("(define (myfn x y)\n(if (> x y 123)\nx\ny))")
lexer("(define (myfn x y) (if (> x y 123) x y))")
