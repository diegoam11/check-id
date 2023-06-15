import cv2
import os

dataPath = 'C:/Users/diego/OneDrive/CICLO 5/Requiremend Engineering/check_id/src/data'
imagePaths = os.listdir(dataPath)
print('imagePaths= ', imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer.read('../modelEigenFace.xml')

cap = cv2.VideoCapture('../diego.mp4')

faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aux_frame = gray.copy()

    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = aux_frame[y: y + h, x: x + w]
        face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(face)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1):
        break

cap.release()
cv2.destroyAllWindows()

