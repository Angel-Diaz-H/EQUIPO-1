#Módulos:
import datetime as dt           # Módulo para utilizar formato fechas.
import os                       # Módulo para limpiar pantalla
from tabulate import tabulate   # Módulo para dar formato tabular.
                                # Si marca error es necesario ejecutar en el símbolo de sistema la siguiente línea: pip install tabulate
import re                       # Módulo para expresiones regulares.
                                # Lo utilizamos para saber si el texto ingresado tenía decimales
import unicodedata              # Módulo para eliminar acentos y caracteres especiales.

#Funciones:
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def guiones(longitud):
    return '-' * longitud

def respuesta_SI_NO(procesar_SI_NO):
    procesar_SI_NO = procesar_SI_NO.strip()
    procesar_SI_NO = procesar_SI_NO.upper()
    procesar_SI_NO = ''.join((c for c in unicodedata.normalize('NFD', procesar_SI_NO) if unicodedata.category(c) != 'Mn'))
    return procesar_SI_NO

def menuActual(numeroMenu, descripcionMenu):
    print(f"Usted se encuentra en la opción {numeroMenu}:\n{guiones(10)}{descripcionMenu.upper()}{guiones(10)}")

def guiones_separadores():
    return print('-' * 50)

#Listas:
lista_menu = [('Número de opción', 'Servicio'),
              (1, 'Registrar nota.'),
              (2, 'Consulta y reportes.'),
              (3, 'Cancelar una nota'),
              (4, 'Recuperar una nota'),
              (5, 'Salir')]

#Recolección de datos:
fecha_actual = dt.date.today()
nota_final = {}
notas_canceladas = []
lista_servicios = []

while True:
    #Menú principal:
    print(f'{guiones(20)}TALLER MECÁNICO DON HAMBLETON{guiones(20)}')
    print('Buen día, ingrese el número de la opción que desee realizar:')
    print(tabulate(lista_menu, headers = 'firstrow', tablefmt = 'pretty'))

    while True:
        try:
            menu = int(input('Opción: '))
            if menu >= 1 and menu <= 5:
                break
            else:
                print("\nIngrese una opción válida del 1 al 5.")
                continue
        except ValueError:
            print("\nIngrese un número válido.")
            continue

    #Registrar nota:
    total_precio_servicio = 0.00
    if menu == 1:
        numero_servicio = 0
        limpiar_consola()
        menuActual(menu, lista_menu[menu][1])
        
        #Folio:
        nueva_nota = (max(nota_final.keys(), default = 0)) + 1
        print(f'\nNúmero de folio creado: {nueva_nota}')
        guiones_separadores()

        #Fecha:
        while True:
            fecha_registro = input("Ingrese la fecha de la realización de la nota (dd/mm/aaaa): ")
            fecha_registro = fecha_registro.strip()

            try:
                fecha_procesada = dt.datetime.strptime(fecha_registro, "%d/%m/%Y").date()
                if fecha_procesada > fecha_actual:
                    print("\nLa fecha no debe ser posterior a la fecha actual. Ingrese una fecha válida.")
                    continue
                break
            except ValueError:
                print("\nIngrese una fecha válida en formato dd/mm/aaaa.")
        guiones_separadores()

        #Nombre del cliente:
        while True:
            nombre_cliente = input('Ingrese el nombre completo del cliente: ')

            if len(nombre_cliente) < 5 or len(nombre_cliente) > 50:
                print("\nEl nombre completo debe tener entre 5 y 50 caracteres.")
                continue

            if not nombre_cliente.replace(' ', '').isalpha():
                print("\nEl nombre solo debe contener letras y espacios.")
                continue
            
            nombre_cliente = nombre_cliente.strip()
            nombre_cliente = nombre_cliente.upper()
            break
        guiones_separadores()

        
        #RFC
    while True:
        print('Tipo de RFC: \n1-Física \n2-Moral ')
        while True:
            try:
                tipo = int(input('Tipo: '))
                if tipo >= 1 and tipo <= 2:
                    break
                else:
                    print("\nIngrese una opción válida del 1 al 2.")
                    continue
            except ValueError:
                print("\nIngrese un número válido.")
                continue  
        guiones_separadores()
        while True:
            if tipo == 1:
                rfc = input('RFC: ')
                if rfc.strip() == '':
                    print('El dato no puede omitirse, intente de nuevo.')
                    continue
                if not re.match(r'^[A-Z]{4}[0-9]{2}[0-9]{2}[0-9]{2}[A-Z0-9]{3}$', rfc):
                    print('El RFC no cumple con el formato esperado.\nNombre(4 iniciales) \nFecha de nacimiento(YYMMDD) \nHomoclave unica')
                    continue
                break
            elif tipo == 2:
                rfc = input('RFC: ')
                if rfc.strip() == '':
                    print('El dato no puede omitirse, intente de nuevo.')
                    continue
                if not re.match(r'^[A-Z]{3}[0-9]{2}[0-9]{2}[0-9]{2}[A-Z0-9]{3}$', rfc):
                    print('El RFC no cumple con el formato esperado.\nNombre(3 iniciales) \nFecha de nacimiento(YYMMDD) \nHomoclave unica')
                    continue
                break
        break
    guiones_separadores()
        #Correo Electronico
        print('Ingrese el correo electronico del cliente: ')
        while True:
            mail = input('Correo Electronico: ')
            if mail.strip() == '':
                print('El dato no puede omitirse. Intente de nuevo.')
                continue
            if not re.match(r'^(?=.{1,256}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',mail):
                print('El correo no es valido. Intente de nuevo.')
                continue
            break
        guiones_separadores()

        #Servicios realizados        
        while True:
            numero_servicio += 1
            #Guardar un servicio:
            #Servicio
            print('Ingrese el nombre del servicio')
            while True:
                servicio = input('Servicio: ').upper()
                if servicio.strip() == '':
                    print('El dato no puede omitirse. Intente de nuevo')
                    continue
                else:
                    break
            guiones_separadores()

            #Precio
            print("Ingrese el precio real del servicio (exactamente con dos decimales): ")                        
            while True:
                recibido_precio_servicio = input("Precio: ")
                recibido_precio_servicio = recibido_precio_servicio.strip()
                if re.match(r'^\d+\.\d{2}$', recibido_precio_servicio):
                    precio_servicio = float(recibido_precio_servicio)
                    break
                else:
                    print("\nIngrese un precio válido, exactamente con dos decimales.")
                    continue
            
            print(f"{guiones(50)}\nServicio agregado correctamente.")

            #Guardar todos los servicios y precios:
            tupla_servicio_actual = (servicio, precio_servicio)
            lista_servicios.append(tupla_servicio_actual)
            total_precio_servicio += precio_servicio

            #Conocer si desea agregar más servicios y llevarlo a su elección:
            print('\t¿Desea agregar otro servicio? (Sí/No)')
            while True:
                otro_servicio = input('\tRespuesta: ')
                otro_servicio = respuesta_SI_NO(otro_servicio)

                if otro_servicio == 'SI' or otro_servicio == 'NO':
                    break
                else:
                    print('\n\tIngrese una respuesta válida (Sí/No).')
            
            if otro_servicio == 'SI':
                limpiar_consola()
                print(f"{numero_servicio} servicio guardado correctamente.\n\n")
                guiones_separadores()
                continue
            else:
                limpiar_consola()
                nota_final[nueva_nota]=(fecha_procesada, nombre_cliente, rfc, mail, lista_servicios, total_precio_servicio)
                #Nota:
                print(f"{guiones(15)}Nota guardada correctamente{guiones(15)}")
                print(f"Información guardada de la nota: {nueva_nota}\n")
                print(tabulate([(nueva_nota, nota_final[nueva_nota][0].strftime("%d/%m/%Y"), nota_final[nueva_nota][1], nota_final[nueva_nota][2],
                                nota_final[nueva_nota][3], nota_final[nueva_nota][5])],
                               headers=['Folio', 'Fecha', 'Cliente','RFC', 'Correo Electronico', 'Monto a Pagar'], tablefmt='pretty'))
                #Detalles de la nota:
                print(f"\nDetalles de la nota:\n{tabulate(lista_servicios, headers = ['Detalle', 'Precio'], tablefmt = 'pretty')}")
                input(f"\n\nDe clic en Enter para continuar.")
                limpiar_consola()
                lista_servicios = []
                tupla_servicio_actual = ()
                break
