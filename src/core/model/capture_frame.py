import cv2
import os
import imutils

class CaptureFrame:
    def __init__(self, id):
        self.id = id
        self.data_path = 'data'
        self.id_path = os.path.join(self.data_path, str(self.id))

        if not os.path.exists(self.id_path):
            os.makedirs(self.id_path)

        self.cap = cv2.VideoCapture(0)
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.count = 0

    def capture_faces(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aux_frame = frame.copy()

            faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face = aux_frame[y: y + h, x: x + w]
                face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(os.path.join(str(self.id_path), 'face_{}.jpg'.format(self.count)), face)
                self.count += 1

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or self.count >= 300 :
                break
    def release_resources(self):
        self.cap.release()
        cv2.destroyAllWindows()
