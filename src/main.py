from model import *
from barcode import *
from database.tables import *
from database.connection import Database

def sub_menu_options():
    print('1. Create student dataset')
    print('2. Retrain model')
    print('3. Go back')
    return int(input("Select option: "))

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
            print('Coming back...')
            break

        else:
            print('This option does not exit, try again.')

def menu_options():
    print('::::::: checkID :::::::')
    print("1. Start")
    print("2. Administrator | Retrain model")
    print('3. Manage database')
    print("4. Exit")
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
                if face_recognition.validated:
                    date = CurrentDate()
                    registration = Registration(id, date.get_current_date(), date.get_current_time())
                    db.insert_registration(registration)
                else:
                    print("The face does not match. ")
            else:
                print('You are not from this university.')

        elif option == 2:
            sub_menu()

        elif option == 3:
            db = Database()
            # create tables: student and registration
            db.create_tables()
            # create a database using webscraping

        elif option == 4:
            print("Exiting the system...")
            break

        else:
            print('This option does not exit, try again.')

if __name__ == '__main__':
    menu()
