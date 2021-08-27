# Escribe tus funciones abajo de esta línea
def pies_cm(pies):
    cm = pies*30.48
    return cm

def pulgadas_cm(pulgadas):
    cm = pulgadas*2.54
    return cm

def yardas_cm(yardas):
    cm = yardas*91.44
    return cm

def main():
    # Escribe tu código abajo de esta línea
    mensaje_inicial = '1. pies a cm, 2. pulgadas a cm, 3. yardas a cm'
    print(mensaje_inicial)
    conversion = int(input('Introduce una opcion: '))
    cant = int(input('Introduce la cantidad: '))
    if cant>0:
        if conversion == 1:
            print(pies_cm(cant))
        elif conversion == 2:
            print(pulgadas_cm(cant))
        elif conversion == 3:
            print(yardas_cm(cant))
        else:
            print('Error')
    else:
        print('Error')
            
if __name__ == '__main__':
    main()
