from src.core.model import *
from src.core.barcode import *
from src.core.date import *
from src.core.webscraping import *
from database.tables import *
from database.database import Database

def sub_menu_options():
    print('1. Capturar fotos de estudiante')
    print('2. Actualizar sistema')
    print('3. Regresar')
    return int(input('Seleccionar opción: '))

def sub_menu():
    while True:
        opt = sub_menu_options()

        if opt == 1:
            print('Por favor, muestre el cósigo de barras del carnet...')
            barcode_detector = BarcodeDetector()
            barcode_detector.detect_barcodes()
            student_id = barcode_detector.get_id()
            db = Database()

            if db.student_exists(student_id):
                print('Este proceso es solo para nuevos estudiantes...')
            else:
                web_scraper = WebScraper(student_id)
                web_scraper.initialize_driver()
                student = web_scraper.scrape_student_data()

                db.insert_student(student)
                web_scraper.close_driver()
                print(student.name, ' agregado a la base de datos!')

                print('Para tomar fotos de tu rostro, por favor mire la cámara...')
                capture_frame = CaptureFrame(student_id)
                capture_frame.capture_faces()
                capture_frame.release_resources()
                print('Capturas de imágenes guardadas!')

        elif opt == 2:
            face_trainer = FaceRecognitionTrainer()
            face_trainer.train_model()

        elif opt == 3:
            print('Regresando...')
            break

        else:
            print('Esta opción no existe, inténtalo de nuevo.')

def menu_options():
    print('::::::: checkID :::::::')
    print('1. Comenzar')
    print('2. Opciones de administrador')
    print('3. Crear base de datos')
    print('4. Salir')
    return int(input('Seleccione una opción: '))

def menu():
    while True:
        option = menu_options()
        if option == 1:

            barcode_detector = BarcodeDetector()
            barcode_detector.detect_barcodes()
            id = int(barcode_detector.get_id())
            db = Database()
            if db.student_exists(id):
                print('Código validado')
                face_recognition = FaceRecognition(id)
                face_recognition.load_model()
                face_recognition.recognize_faces()
                if face_recognition.validated:
                    date = CurrentDate()
                    registration = Registration(id, date.get_current_date(), date.get_current_time())
                    db.insert_registration(registration)
                    print('Acceso otorgado!')
                else:
                    print('El rostro no coincide')
            else:
                print('No eres de esta universidad')

        elif option == 2:
            sub_menu()

        elif option == 3:
            db = Database()
            db.create_tables()
            student1 = Student(21200026, 'rodrigo davila vasquez', 'ingeniería de software')
            student2 = Student(21200195, 'Kevin tupac aguero', 'ingeniería de software')
            db.insert_student(student1)
            db.insert_student(student2)

        elif option == 4:
            print('Saliendo del sistema...')
            break

        else:
            print('Esta opción no existe, intténtalo de nuevo')

if __name__ == '__main__':
    menu()
