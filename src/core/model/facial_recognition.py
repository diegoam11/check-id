import cv2
import os


class FaceRecognition:
    def __init__(self, code_from_id):
        self.data_path = 'data'
        self.model_path = 'modelEigenFace.xml'
        self.image_paths = os.listdir(self.data_path)
        self.face_recognizer = cv2.face.EigenFaceRecognizer_create()
        self.faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        self.validated = False
        self.countValidation = 0
        self.code_from_id = code_from_id
        self.coincide = True
        self.countNoCoincide = 0

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
                if int(self.image_paths[result[0]]) != self.code_from_id:
                    self.coincide = False
                    self.countNoCoincide += 1

                cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

                if result[1] < 5000:
                    cv2.putText(frame, '{}'.format(self.image_paths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    self.countValidation += 1
                else:
                    cv2.putText(frame, 'Unidentified', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or self.countValidation >= 15:
                self.validated = True
                break

            if self.coincide == False and self.countNoCoincide > 10 :
                print('No coincide la información del carnet con su rostro')
                break

        cap.release()
        cv2.destroyAllWindows()
