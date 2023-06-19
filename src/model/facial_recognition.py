import cv2
import os


class FaceRecognition:
    def __init__(self):
        self.data_path = 'C:/Users/diego/OneDrive/CICLO 5/Requiremend Engineering/check_id/src/data'
        self.model_path = 'modelEigenFace.xml'
        self.face_recognizer = cv2.face.EigenFaceRecognizer_create()
        self.faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        self.validated = False

    def load_data(self):
        image_paths = os.listdir(self.data_path)
        print('imagePaths= ', image_paths)

    def load_model(self):
        self.face_recognizer.read(self.model_path)

    def recognize_faces(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aux_frame = gray.copy()

            faces = self.faceClassifier.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                face = aux_frame[y: y + h, x: x + w]
                face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
                result = self.face_recognizer.predict(face)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


