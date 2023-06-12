import cv2
import os
import imutils


personName = "diego"
dataPath = "C:/Users/diego/OneDrive/CICLO 5/Requiremend Engineering/check_id/src/data"
personNamePath = dataPath + "/" + personName

if not os.path.exists(personNamePath):
    os.makedirs(personNamePath)

cap = cv2.VideoCapture('../../diego.mp4')

faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
count = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face = auxFrame[y: y+h, x:x+w]
        face = cv2.resize(face, (150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personNamePath + '/face_{}.jpg'.format(count), face)
        count = count + 1

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27 or count >= 300:
            break

cap.release()
cv2.destroyAllWindows()

