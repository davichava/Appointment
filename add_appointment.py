import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '+3cN1c0',
    database = 'appointment'
)

cursor = conexion.cursor()

def Appointment():

    class Appointment():
        def __init__(self, identification_pct, name_pct, lastname_pct, phone, email, address, barrium, city, country):
            self.identification_pct = identification_pct
            self.name_pct = name_pct
            self.lastname_pct = lastname_pct            
            self.phone = phone
            self.email = email
            self.address = address
            self.barrium = barrium
            self.city = city            
            self.country = country

    # crear_carpeta()

    mostrar_menu()
    
    confir = True
    while confir:
        opcion = input('Seleciona Una Opcion: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            add_appointment()
            confir = False
        elif opcion == 2:
            view_appointment()
            confir = False
        elif opcion == 3:
            search_appointment()
            confir = False
        elif opcion == 4:
            update_appointment()
            confir = False
        elif opcion == 5:
            delete_appointment()
            confir = False
        elif opcion == 6:
            print('Saliste Del Programa')
            break
        else:
            print('No Entiendo Lo Que Quieres Hacer')

def mostrar_menu():
    print('Elige Una Opcion\n')
    print(f'1) Agregar Cita \n')
    print(f'2) Ver Cita \r\n')
    print(f'3) Consultar Cita \n')
    print(f'4) Actualizar Cita \n')
    print(f'5) Eliminar Cita \n')
    print(f'6) Salir del Programa \n')

def add_appointment():
    print('Digite El Numero De Cedula: \r\n')
    identification_pct = input('Digita Tu Cedula: \r\n')

   
    existe = existe_patient(identification_pct)
    if not existe:
        nuevo_usuario = (3268426, 'Pepito', 'Perez', 30048625,'pepito@gmail.com','cr 17-452-45','itagui','Medellin','Colombia')
        consulta = ('INSERT INTO appointment.date_pct '
                    '(identification_pct, name_pct, lastname_pct, phone, email, address, barrium, city, country) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')
    else:
        print('Paciente Ya Existe...')
  

    cursor.execute(consulta, nuevo_usuario)

    conexion.commit()

    print('Registro guardado')

    conexion.close()  
    Appointment()
def view_appointment():
    print('ACA')

def search_appointment():
    print('ACA')
def update_appointment():
    print('ACA')
def delete_appointment():
    print('ACA')

# def crear_carpeta():
#     if not os.path.exists('Appointment/'):
#         os.makedirs('Appointment/')

def existe_patient(identification_pct):
    return 

Appointment()