import cv2
import pytesseract
import re


class Frame:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def set_resolution(self, width: int, height: int):
        self.cap.set(3,width)
        self.cap.set(4, height)

    def read(self):
        while True:
            ret, frame = self.cap.read()
            t = cv2.waitKey(1)
            cv2.imshow("ID INTELIGENTE", frame)
            if t == 27:
                break

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
