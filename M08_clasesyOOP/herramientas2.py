class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def _comprobar(self):
        for i in self.lista:
            if (self.comprobar(i)):
                print('El numero', i, 'es primo')
            else:
                print('El numero', i, 'no es primo')

    def comprobar(self, numero):
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        return primo
    
    def _conver_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.conver_grados(i, origen, destino), 'grados', destino)

    def _factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.factorial(i))

    def lista_num(self, num):
        principal = []
        repetidos = []
        if len(self.lista) == 0:
            return None
        if (num):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in principal:
                i = principal.index(elemento)
                repetidos[i] += 1
            else:
                principal.append(elemento)
                repetidos.append(1)
        moda = principal[0]
        maximo = repetidos[0]
        for i, elemento in enumerate(principal):
            if repetidos[i] > maximo:
                moda = principal[i]
                maximo = repetidos[i]
        return moda, maximo
    
    def conver_grados(self, valor, origen, destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor  
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32  
            elif destino == 'kelvin':
                valor_destino = valor + 273.15  
            else:
                print('Dato de Destino incorrecto')
        elif  origen == 'farenheit':
            if destino == 'farenheit':
                valor_destino = valor  
            elif destino == 'celsius':
                valor_destino = (valor -32) * 5 / 9  
            elif destino == 'kelvin':
                valor_destino = ((valor -32) * 5 / 9 ) + 273.15  
            else:
                print('Dato de Destino incorrecto')
        elif origen == 'kelvin':
            if destino == 'kelvin':
                valor_destino = valor  
            elif destino == 'celsius':
                valor_destino = valor - 273.15 
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32  
            else:
                print('Dato de Destino incorrecto')
        else:
            print('Dato de Origen incorrecto') 
        return valor_destino
    
    def factorial(self, numero):
        if type(numero) != int:
            return 'El número debe ser un entero'
        elif numero < 0:
            return 'El numero debe ser positivo'
        elif numero <= 1:
            return 1
    
        numero = numero * self.factorial(numero - 1)
        return numero
    