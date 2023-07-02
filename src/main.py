from src.core.model import *
from src.core.barcode import *
from src.core.date import *
from src.core.webscraping import *
from database.tables import *
from database.database import Database

def sub_menu_options():
    print('1. Capture student photos')
    print('2. Update model')
    print('3. Go back')
    return int(input("Select option: "))

def sub_menu():
    while True:
        opt = sub_menu_options()

        if opt == 1:
            # test
            student_id = int(input('id: '))
            print('To take photos of your face, please look at the camera...')
            capture_frame = CaptureFrame(student_id)
            capture_frame.capture_faces()
            capture_frame.release_resources()
            print('Saved face shots!')
            # test

            '''
            print('Please show your university ID...')
            barcode_detector = BarcodeDetector()
            barcode_detector.detect_barcodes()
            student_id = barcode_detector.get_id()
            db = Database()

            if db.student_exists(student_id):
                print('This process is for new students only...')
            else:
                web_scraper = WebScraper(student_id)
                web_scraper.initialize_driver()
                student = web_scraper.scrape_student_data()

                db.insert_student(student)
                web_scraper.close_driver()
                print(student.name, ' added to student database!')

                print('To take photos of your face, please look at the camera...')
                capture_frame = CaptureFrame(student_id)
                capture_frame.capture_faces()
                capture_frame.release_resources()
                print('Saved face shots!')
            '''

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
    print("2. Administrator options")
    print("3. Create database")
    print("4. Exit")
    return int(input("Select option: "))

def menu():
    while True:
        option = menu_options()
        if option == 1:
            # test
            face_recognition = FaceRecognition()
            face_recognition.load_model()
            face_recognition.recognize_faces()
            # test

            '''
            barcode_detector = BarcodeDetector()
            barcode_detector.detect_barcodes()
            id = int(barcode_detector.get_id())
            db = Database()
            if db.student_exists(id):
                face_recognition = FaceRecognition()
                face_recognition.load_model()
                face_recognition.recognize_faces()
                face_recognition.validated = True
                if face_recognition.validated:
                    date = CurrentDate()
                    registration = Registration(id, date.get_current_date(), date.get_current_time())
                    db.insert_registration(registration)
                else:
                    print("The face does not match. ")
            else:
                print('You are not from this university.') 
            '''

        elif option == 2:
            sub_menu()

        elif option == 3:
            db = Database()
            db.create_tables()
            piero = Student(21200021, 'PIERO BAYONA MORE', 'MEDICINA')
            diego = Student(21200022, 'DIEGO ALVAREZ MORE', 'SOFTWARE')
            db.insert_student(piero)
            db.insert_student(diego)

        elif option == 4:
            print("Exiting the system...")
            break

        else:
            print('This option does not exit, try again.')

if __name__ == '__main__':
    menu()
