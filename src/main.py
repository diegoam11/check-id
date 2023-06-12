from model import *


def menu_options():
    print('Reentrenar modelo')
    print("1. Crear dataset de alumno")
    print("2. Entrenar modelo")
    opt = int(input("Select option: "))
    return opt


def menu():
    while True:
        option = menu_options()
        if option == 1:
            person_name = "Diego"
            data_path = "C:/Users/diego/OneDrive/CICLO 5/Requiremend Engineering/check_id/src/data"
            face_recognition = FaceRecognition(person_name, data_path)
            face_recognition.capture_faces()
            face_recognition.release_resources()

        elif option == 2:
            data_path = "C:/Users/diego/OneDrive/CICLO 5/Requiremend Engineering/check_id/src/data"
            face_trainer = FaceRecognitionTrainer(data_path)
            face_trainer.train_model()

        else:
            print("This option doesn't exists")


if __name__ == '__main__':
    menu()
