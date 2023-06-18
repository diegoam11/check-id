from model import *
from barcode import *
from database.tables import *
from database.connection import Database

def sub_menu_options():
    print('1. Crear data set de estudiante')
    print('2. Re entrenar modelo')
    print('3. Regresar')
    return int(input("Ingrese una opcion: "))

def sub_menu():
    while True:
        opt = sub_menu_options()

        if opt == 1:
            person_name = input('Enter name: ')
            capture_frame = CaptureFrame(person_name)
            capture_frame.capture_faces()
            capture_frame.release_resources()

        elif opt == 2:
            face_trainer = FaceRecognitionTrainer()
            face_trainer.train_model()

        elif opt == 3:
            print('Regresando...')
            break

        else:
            print('Esta opción no existe, vuelva a intentarlo')

def menu_options():
    print('::::::: checkID :::::::')
    print("1. Start")
    print("2. Administrador | Re entrenar modelo")
    print('3. Gestionar base de datos')
    print("4. Salir")
    return int(input("Select option: "))

def menu():
    while True:
        option = menu_options()
        if option == 1:
            barcode_detector = BarcodeDetector()
            barcode_detector.detect_barcodes()
            id = int(barcode_detector.get_id())
            db = Database()
            if db.student_exists(id):
                face_recognition = FaceRecognition()
                face_recognition.load_data()
                face_recognition.load_model()
                face_recognition.recognize_faces()
            else:
                print('No perteneces a esta universidad')

        elif option == 2:
            sub_menu()

        elif option == 3:
            db = Database()
            # create tables: student and registration
            db.create_tables()
            # create a database using webscraping
            student = Student(21200022, 'Diego', 'Engineering ')
            db.insert_student(student)
            registration = Registration(21200022, '2023-06-14', '09:00:00', '17:00:00')
            db.insert_registration(registration)

        elif option == 4:
            print("Saliendo del sistema...")
            break

        else:
            print('Esta opción no existe, vuelva a intentarlo')

if __name__ == '__main__':
    menu()
