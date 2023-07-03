#Ejercicio: Sistema de gestión de empleados
#Escribe un programa en Python que permita gestionar los empleados de una empresa mediante un menú de opciones. Cada empleado tiene un nombre, 
# un salario y una posición en la empresa (por ejemplo, "Gerente", "Supervisor", "Analista", etc.).
#El programa debe tener las siguientes características:
#Utiliza herencia para crear una clase "Empleado" y dos subclases "Gerente" y "Empleado de oficina", con atributos y métodos específicos para cada tipo de empleado.
#Utiliza polimorfismo para implementar un método "calcular salario" que devuelva el salario correspondiente a cada tipo de empleado.
#Utiliza una lista para almacenar todos los empleados y un bucle para permitir al usuario agregar, eliminar y modificar empleados.
#Crea una función para imprimir la lista de empleados con sus respectivos nombres, salarios y posiciones en la empresa.
#Crea un menú con las opciones "Agregar empleado", "Eliminar empleado", "Modificar empleado", "Mostrar lista de empleados" y "Salir".
#Utiliza una estructura de control de flujo "while" para permitir al usuario seleccionar una opción del menú y ejecutar las acciones correspondientes 
# hasta que se seleccione la opción "Salir".
import logging
class Empleado:

    def __init__(self,nombre,apellido,dni,salario,posición,):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario 
        self.posición = posición
    
    def __str__(self):
        return "Mi nombre es "+str(self.nombre)+" "+str(self.apellido)+". Soy "+str(self.posición)+"."
    

class Gerente(Empleado):   
    def __init__(self, nombre, apellido, dni, salario,bono):
        self.bono=bono
        super().__init__(nombre, apellido, dni, salario, "Gerente")
    
    def __str__(self):
        return super().__str__() +" Mi bono es de "+str(self.bono)+"$"

    def calcular_salario_anual (self):
        salario= "El salario anual de "+str(self.nombre)+" "+str(self.apellido)+" es de: "+str((self.salario*12) + (self.bono*12))+"$."
        return salario


class Empleado_de_oficina(Empleado):

    def __init__(self, nombre, apellido, dni, salario,horas_extra):
        self.horas_extra=horas_extra
        self.tareas= []
        self.solicitud = 0
        super().__init__(nombre, apellido, dni, salario, "Empleado de oficina")

    def __str__(self):
        return super().__str__() +" Tengo que hacer "+str(self.horas_extra)+" horas extra."

    def realizar_tareas(self,dni,lista_total):
        for i in lista_total:
            if i.dni == dni:
                if len(i.tareas) == 0:
                    break
                else:
                    i.tareas = []
                    print ("¡Todas las tareas realizadas con éxito!.")

    def ver_tareas(self):
        tareas_pendientes=self.tareas
        return "Tareas pendientes: "+tareas_pendientes+"."
        
    def calcular_salario_anual (self):
        salario= "El salario anual de "+str(self.nombre)+" "+str(self.apellido)+"es de "+str(self.salario*12)+"$."
        return salario
    
    def pedir_vacaciones(self,dni,días_a_pedir,lista):
        encontrado = False
        for i in lista:
            if i.dni == dni:
                encontrado = True
                i.solicitud = días_a_pedir
        if not encontrado:
            print("No se encontró el DNI registrado")
            return
                


class Empresa():
    def __init__(self,lista_empleados,lista_gerentes,lista_total):
        self.lista_empleados =lista_empleados
        self.lista_gerentes=lista_gerentes
        self.lista_total=lista_total
    
    def agregar_gerente(self,empleado):
        for i in self.lista_total:
            if i.dni == empleado.dni:
                print("El DNI ya se encuentra registrado en la base de datos.")
                return 
        self.lista_gerentes.append(empleado)
        self.lista_total.append(empleado)
        
    def agregar_empleado_de_oficina(self,empleado):
        for i in self.lista_total:
            if i.dni == empleado.dni:
                print("El DNI ya se encuentra registrado en la base de datos.")
                return
        self.lista_empleados.append(empleado)
        self.lista_total.append(empleado)
        
    def buscar_empleado(self,dni):
        for empleado in self.lista_total:
            if empleado.dni == dni:
                return empleado
        return "el DNI buscado no esta registrado." 

    def eliminar_empleado(self, dni):
        encontrado = False
        for i in self.lista_total:
            if i.dni == dni:
                encontrado = True
                if confirmar("Seguro que desea eliminar a "+i.nombre+" "+i.apellido+" ("+str(i.dni)+")?"):
                    if i.posición == "Gerente":
                        self.lista_total.remove(i)
                        self.lista_gerentes.remove(i)
                        print("Gerente eliminado correctamente")
                        return
                    else:
                        self.lista_total.remove(i)
                        self.lista_empleados.remove(i)
                        print("Empleado de oficina eliminado correctamente")
                        return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return

    def  calcular_salario(self, dni):
        encontrado = False
        for i in self.lista_total:
            if i.dni == dni:
                encontrado = True
                if i.posición == "Gerente":
                    salario =Gerente.calcular_salario_anual(i)
                    print(salario)
                    return
                else: 
                    salario = Empleado_de_oficina.calcular_salario_anual(i)
                    print (salario)
                    return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return

    def modificar_empleado(self, dni):
        encontrado = False
        for i in self.lista_total:
            if i.dni == dni:
                encontrado = True
                if i.posición == "Gerente":
                    while True:
                        print("¿Que dato desea modificar?")
                        print("1. Nombre")
                        print("2. Apellido")
                        print("3. DNI")
                        print("4. Bono")
                        print("5. Salir")
                        respuesta=input("Selecciona el número:")
                        if respuesta == "1":
                            nombre= validar_letras(input("Ingrese el nombre: "))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el nombre de "+i.nombre+" a "+nombre+"?: "):
                                i.nombre=nombre
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "2":
                            apellido = validar_letras(input("ingrese el apellido: "))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el nombre de "+i.apellido+" a "+apellido+"?: "):
                                i.apellido = apellido
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "3":
                            dni_nuevo = validar_dni(input("Ingrese el dni: "))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el dni "+str(i.dni)+" a "+str(dni_nuevo)+"?: "):
                                i.dni=dni_nuevo
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "4":
                            bono = validar_números_no_enteros(input("Ingrese el bono:"))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el bono de "+str(i.bono)+"$ a "+str(bono)+"$?: "):
                                i.bono=bono
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "5":
                            break
                        else:
                            logging.error("Debe introducir un número que aparezca en las opciones.")
                    return
                if i.posición == "Empleado de oficina":
                    while True:
                        print("¿Que dato desea modificar?")
                        print("1. Nombre")
                        print("2. Apellido")
                        print("3. DNI")
                        print("4. Horas extra:")
                        print("5. Salir")
                        respuesta=input("Selecciona el número:")
                        if respuesta == "1":
                            nombre= validar_letras(input("Ingrese el nombre: "))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el nombre de "+i.nombre+" a "+nombre+"?: "):
                                i.nombre=nombre
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "2":
                            apellido = validar_letras(input("ingrese el apellido: "))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el nombre de "+i.apellido+" a "+apellido+"?: "):
                                i.apellido = apellido
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "3":
                            dni_nuevo = validar_dni(input("Ingrese el dni"))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar el dni "+str(i.dni)+" a "+str(dni_nuevo)+"?: "):
                                i.dni=dni_nuevo
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "4":
                            horas_extra = validar_números_enteros(input("Ingrese las horas extra:"))
                            logging.warning("!CUIDADO¡")
                            if confirmar("Esta seguro de cambiar las horas extra de "+str(i.horas_extra)+" a "+str(horas_extra)+"?: "):
                                i.horas_extra=horas_extra
                            else:
                                logging.warning("Cambio no realizado.")
                        elif respuesta == "5":
                            break
                        else:
                            logging.error("Debe introducir un número que aparezca en las opciones.")    
                    return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return

    def mostrar_lista_gerente(self):
    # Recorrer la lista de empleados
        for gerente in self.lista_gerentes:
            print(f"Nombre: {gerente.nombre} {gerente.apellido}")
            print(f"DNI: {gerente.dni}")
            print(f"Salario: {gerente.salario}")
            print(f"Bono: {gerente.bono}")

    def mostrar_lista_empleados_oficina(self):
    # Recorrer la lista de empleados
        for empleado in self.lista_empleados:
            print(f"Nombre: {empleado.nombre} {empleado.apellido}")
            print(f"DNI: {empleado.dni}")
            print(f"Salario: {empleado.salario}")
            print(f"Horas extra: {empleado.horas_extra}")
    
    def mostrar_lista_total(self):
        for empleado in self.lista_total:
            if isinstance(empleado, Gerente):
                print(f"Nombre: {empleado.nombre} {empleado.apellido}")
                print(f"DNI: {empleado.dni}")
                print(f"Salario: {empleado.salario}")
                print(f"Bono: {empleado.bono}")
                print(f"Posición: {empleado.posición}\n")
            elif isinstance(empleado, Empleado_de_oficina):
                print(f"Nombre: {empleado.nombre} {empleado.apellido}")
                print(f"DNI: {empleado.dni}")
                print(f"Salario: {empleado.salario}")
                print(f"Horas extra: {empleado.horas_extra}")
                print(f"Posición: {empleado.posición}\n")
    
    def mostrar_tareas_empleados_oficina(self,dni):
        for i in self.lista_total:
            if i.dni == dni:
                if len(i.tareas) == 0:
                    print("No hay tareas asignadas al empleado "+str(i.nombre)+".")
                else:
                    print("Tareas de "+str(i.nombre)+" "+str(i.apellido)+":")
                    print(i.tareas)
    
    def mostrar_solicitud_empleado(self,dni):
        for i in self.lista_total:
            if i.dni == dni:
                if i.solicitud == 0:
                    print("No hay solicitud del empleado "+str(i.nombre)+".")
                else:
                    print("El empleado "+str(i.nombre)+" "+str(i.apellido)+" solicito "+str(i.solicitud)+" días de vacaciones")
    
    def dar_tareas(self,dni):
        encontrado = False
        for i in self.lista_total:
            if i.dni == dni:
                encontrado = True
                tarea= input("Escribe la tarea que quieres asignarle: ")
                i.tareas.append(tarea)
                print("¡Tarea agregada con éxito!")
                return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return

    def aprobar_días_libres(self,dni):
        encontrado = False
        for i in self.lista_empleados:
            if i.dni == dni:
                encontrado = True
                print("Solicitud aprobada, que tenga unas buenas vacaciones")
                i.solicitud = 0
                return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return
    
    def rechazar_días_libres(self,dni):
        encontrado = False
        for i in self.lista_empleados:
            if i.dni == dni:
                encontrado = True
                print("Solicitud rechazada, lo sentimos.")
                i.solicitud = 0
                return
        if not encontrado:
            print("No se encontró el DNI registrado")
            return
        
    def agregar_gerente_o_empleado(palabra):
        palabra = palabra.capitalize()
        while True:
            if palabra == "Gerente":
                bono = validar_números_no_enteros(input("Ingrese el bono del gerente: "))
                empleado = Gerente(nombre,apellido,dni, salario, bono)
                empresa.agregar_gerente(empleado)
                break
            elif palabra == "Empleado de oficina":
                horas_extra = validar_números_no_enteros(input("Ingrese las horas extra del empleado de oficina: "))
                empleado = Empleado_de_oficina(nombre,apellido,dni, salario, horas_extra)
                empresa.agregar_empleado_de_oficina(empleado)
                break
            else:
                print ("Error, posición no valida. Solo se acepta 'Gerente' o 'Empleado de oficina'.")
                palabra = input("Ingrese la posición del empleado: ")
                palabra= palabra.capitalize()


empresa= Empresa([],[],[])
def validar_letras(palabra):
    while True:
        if palabra.replace(" ","").isalpha() == True: #controlamos que sea letras o espacios
            break
        else:
            logging.error("Solo se aceptan letras (no números o caracteres especiales).")
            palabra=input("Ingrese nuevamente el dato: ")
    return palabra.title()

def validar_números_enteros(numero):
    while True:
        if numero.isdigit() == True: #controlamos que sean números
            break
        else:
            logging.error("Solo se aceptan números.")
            numero=input("Ingrese nuevamente el dato: ")
    return int(numero)

def validar_números_no_enteros(numero):
    while True:
        if numero.replace(".","").isdigit() == True : #controlamos que puedan ser números o enteros o flotantes
            break
        else:
            logging.error(" Solo se aceptan números.")
            numero=input("Ingrese el bono del usuario: ")
    return float(numero)

def validar_números_que_pueden_ser_negativos(numero):
    while True:
        if numero.replace(".","").isdigit() == True and numero.replace("-","",1).isdigit() == True: #controlamos que puedan ser números o enteros o flotantes
            break
        else:
            logging.error(" Solo se aceptan números.")
            numero=input("Ingrese el bono del usuario: ")
    return float(numero)

def validar_dni(numero,):
    while True:
        if numero.isdigit() == True and len(numero) >7: 
            break
        else:
            if numero.isdigit() == False:
                logging.error("Solo se aceptan números.")
            else:
                logging.error("Son solamente 8 números.")
            numero=input("Ingrese nuevamente el dato: ")
    return int(numero)

def confirmar(mensaje):
    respuesta = input(mensaje + "Ingrese si o no como respuesta: ")
    while respuesta.lower() not in ['si', 'no']:
        respuesta = input("Respuesta inválida. " + mensaje + " Ingrese si o no como respuesta. ")
    return respuesta.lower() == 'si'

def lista_tiene_elementos(lista):
    return len(lista) > 0

print("¡Bienvenido! ¿Que desea hacer hoy?")    
while True:
    print("Ingrese el número correspondiente a la operación que desea realizar: ")
    print("1. Agregar empleado a la lista")
    print("2. Eliminar empleado de la lista")
    print("3. Editar dato de un empleado")
    print("4. Mostrar lista de personal completo")
    print("5. Mostrar lista de gerentes")
    print("6. Mostrar lista de empleados de oficina")
    print("7. Ver salario anual de un empleado")
    print("8. Asignar tareas a un empleado de oficina")
    print("9. Ver tareas de un empleado de oficina")
    print("10. Elegir un empleado que haga las tareas pendientes")
    print("11. Ver un empleado especifico")
    print("12. Elegir un empleado que pida días libres")
    print("13. Ver solicitudes de vacaciones de un empleado de oficina")
    print("14. Aprobar o días libres")
    print("15. Rechazar días libres")
    print("16. Salir ")
    operación=input("Operación que desea realizar: ")
    print("")
    if operación == "1":
        # Acciones correspondientes a la opción 1
        print("Ha seleccionado la opción 1.\n")
        nombre= validar_letras(input("Ingrese el nombre del empleado: "))
        apellido=validar_letras(input("Ingrese el apellido del empleado: "))
        dni=validar_dni(input("Ingrese el dni del usuario: "))
        salario=validar_números_no_enteros(input("Ingrese el salario del empleado: "))
        posición = empresa.agregar_gerente_o_empleado(input("Ingrese la posición del empleado: "))
    if operación == "2":
        if lista_tiene_elementos(empresa.lista_total):
            print("Ha seleccionado la opción 2.\n")
            print("Lista del personal total de la empresa: \n")
            Empresa.mostrar_lista_total(empresa)
            dni_a_eliminar=validar_dni(input("Ingrese el DNI de la persona que desee eliminar: "))
            empresa.eliminar_empleado(dni_a_eliminar)
        else:
            print("No hay ningún empleado cargado a la lista.")
    if operación == "3":
        print("Ha seleccionado la opción 3.\n")
        if lista_tiene_elementos(empresa.lista_total):
            print("Lista del personal total de la empresa: \n")
            Empresa.mostrar_lista_total(empresa)
            dni_a_modificar= validar_dni(input("Ingrese el DNI de la persona que desea modificar: "))
            empresa.modificar_empleado(dni_a_modificar)
        else:
            print("No hay ningún empleado cargado a la lista.")
    if operación == "4":
        print("Ha seleccionado la opción 4.\n")
        if lista_tiene_elementos(empresa.lista_total):
            print("Lista del personal total de la empresa: \n")
            Empresa.mostrar_lista_total(empresa)
        else:
            print("No hay ningún empleado cargado a la lista.")
    if operación == "5":
        print("Ha seleccionado la opción 5.\n")
        if lista_tiene_elementos(empresa.lista_gerentes):
            print("Lista de los gerentes de la empresa: \n")
            Empresa.mostrar_lista_gerente(empresa)
        else:
            print("No hay ningún gerente.")
    if operación == "6":
        print("Ha seleccionado la opción 6.\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Lista de empleados de oficinas de la empresa: \n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
        else:
            print("No hay ningún empleado de oficina.")
    if operación == "7":
        print("Ha seleccionado la opción 7.\n")
        if lista_tiene_elementos(empresa.lista_total):
            print("Lista de los empleados de oficina de la empresa: \n")
            Empresa.mostrar_lista_total(empresa)
            dni_a_calcular= validar_dni(input("Ingrese el DNI de la persona que desea calcular el salario total: "))
            empresa.calcular_salario(dni_a_calcular)
    if operación == "8":
        print("Ha seleccionado la opción 8.\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Lista de los empleados de oficina de la empresa: \n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
            dni_a_agregar= validar_dni(input("Ingrese el DNI de la persona que desea asignarle una tarea: "))
            empresa.dar_tareas(dni_a_agregar)
        else:
            print("No hay ningún empleado cargado a la lista.")
    if operación =="9":
        print("Ha seleccionado la opción 9.\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Lista de los empleados de oficina de la empresa: \n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
            dni_a_ver= validar_dni(input("Ingrese el DNI de la persona que desea ver sus tareas: "))
            empresa.mostrar_tareas_empleados_oficina(dni_a_agregar)
        else:
            print("No hay ningún empleado cargado a la lista.")      
    if operación == "10":
        print("Ha seleccionado la opción 10\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            Empresa.mostrar_lista_empleados_oficina(empresa)
            print("Seleccione un empleado que tenga tareas pendientes: \n")
            dni = validar_dni(input("Ingrese el DNI del empleado: \n"))
            empleado = empresa.buscar_empleado(dni)
            if isinstance(empleado, str):
                print(empleado)  # muestra el mensaje de error
            else:
                empleado_oficina= Empleado_de_oficina(empleado.nombre,empleado.apellido,empleado.dni,empleado.posición,empleado.horas_extra)
                empleado_oficina.realizar_tareas(dni,empresa.lista_total)
    if operación == "11":
        print("Ha seleccionado la opción 11\n")
        dni= validar_dni(input("Ingrese el dni del empleado que sea ver: "))
        print(empresa.buscar_empleado(dni))
    if operación == "12":
        print("Ha seleccionado la opción 12\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            Empresa.mostrar_lista_empleados_oficina(empresa)
            print("Seleccione un empleado que quiera pedir una solicitud para días libres: \n")
            dni_a_agregar = validar_dni(input("Ingrese el DNI del empleado: \n"))
            empleado = empresa.buscar_empleado(dni)
            if isinstance(empleado, str):
                print(empleado)  # muestra el mensaje de error
            else:
                empleado_oficina= Empleado_de_oficina(empleado.nombre,empleado.apellido,empleado.dni,empleado.posición,empleado.horas_extra)
                solicitud= validar_números_enteros(input("Ingrese el numero de días que solicita de vacaciones: "))
                empleado_oficina.pedir_vacaciones(dni,solicitud,empresa.lista_empleados)
                print("Solicitud enviada.")
    if operación == "13":
        print("Ha seleccionado la opción 13\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Lista de los empleados de oficina de la empresa: \n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
            dni_a_ver= validar_dni(input("Ingrese el DNI de la persona que desea ver su solicitud: "))
            empresa.mostrar_solicitud_empleado(dni_a_ver)
        else:
            print("No hay ningún empleado cargado a la lista.")
    if operación == "14":
        print("Ha seleccionado la opción 14\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Ha seleccionado la opción 14\n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
            dni_a_ver= validar_dni(input("Ingrese el DNI de la persona que desea aprobar su solicitud: "))
            empresa.aprobar_días_libres(dni_a_ver)
        else:
            print("No hay ningún empleado cargado a la lista.") 
    if operación == "14":
        print("Ha seleccionado la opción 14\n")
        if lista_tiene_elementos(empresa.lista_empleados):
            print("Ha seleccionado la opción 14\n")
            Empresa.mostrar_lista_empleados_oficina(empresa)
            dni_a_ver= validar_dni(input("Ingrese el DNI de la persona que desea rechazar su solicitud: "))
            empresa.rechazar_días_libres(dni_a_ver)
        else:
            print("No hay ningún empleado cargado a la lista.") 
    if operación == "16":
        print("Ha seleccionado la opción 14.\n")
        print("Gracias, !Nos vemos pronto¡")
        break


