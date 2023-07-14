letras = ['A','B','C','D']
precio = [ 3.800, 3.000, 2.800, 3.500 ]
depto = []
compradores = []
num_boleta = 1
ganancias = 0

def quitar_signos(run):
    final = ''
    for i in range(0,len(run)):
        if run[i] != '.' and run[i] != '-':
            if len(final) < 8:
                final += run[i]
    return final
    
def imprimir_menu():
    print('******************************')
    print('********* CASA-FELIZ  ********')
    print('[1] Comprar departamento')
    print('[2] Mostrar departamentos')
    print('[3] Ver listado de compradores')
    print('[4] Mostrar ganancias totales')
    print('[5] Salir')
    print('******************************')

def obtener_opc():
    while True:
        try:
            opc = int(input('Seleccione una alternativa: '))
            if opc >= 1 and opc <= 5:
                return opc
            else:
                print('ingrese una alternativa valida')
        except:
            print('error intente nuevamente')
            
def imprimir_depa(depto):

    cont = 1
    for letra in letras:
        if letra == 'A':
            print('  ', end='')
        print(f"  {letra}   ", end='')
    print('')
    
    for fila in depto:
        print(cont , end="")
        cont +=1
        for columna in fila:
            print(f" [{columna}] ", end="")
        
        print('')

def obtener_piso():
    while True:
        try:
            piso = int(input('selecciona la fila del [1-10]: '))
            if piso >= 1 and piso <=10:
                return piso
            else:
                print('selecione la fila del [1-10]')
        except:
            print('error. ingrese nuevamente')

def obtener_columna():
    while True:
        columna_letra = input('seleccione el departamento de la [A-D]: ')

        for p, letra in enumerate(letras):
            if letra == columna_letra:
                return p
                
        print('Error. seleccione letras desde [A-D]')
        
## PROCEDIMIENTOS


for piso in range(10):
    columnas = []
    for columna in range(4):
        columnas.append('🏠')
        
    depto.append(columnas)
    


while True:
    imprimir_menu()
    opc = obtener_opc()
    if opc == 1:
        while True:
            imprimir_depa(depto)
            piso = obtener_piso() - 1
            columna = obtener_columna()
            
            if depto[piso][columna] == '✖️':
                print('***************************')
                print('Error. departamento ya comprado')
                print('elige otro departamento')
                print('***************************')
                input('presione una tecla para continuar --> ')
            else:
                if columna == 'A':
                    ganancias += 3800
                elif columna == 'B':
                    ganancias += 3000
                elif columna == 'C':
                    ganancias += 2800
                else:
                    ganancias += 3500
                    
                depto[piso][columna] = '✖️'
                nombre = input('¿Cual es tu nombre? ')
                run = input('ingrese su run: ')
                rut = quitar_signos(run)
                compradores.append([nombre, rut])
                
                print(f"gracias por adquirir un departamento #{num_boleta}")
                num_boleta += 1
                imprimir_depa(depto)
                break
                
    elif opc == 2:
        imprimir_depa(depto)
        input('presione una tecla para continuar --> ')
        
    elif opc == 3:
        for cliente in compradores:
            print(f'Nombre: {cliente[0]}, Run: {cliente[1]}')             
    elif opc == 4:
        #Mostrar ganancias totales
        print(f"Las ganancias son de {ganancias} UF")
        
    elif opc == 5:
        break
