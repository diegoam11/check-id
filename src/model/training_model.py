import cv2
import os
import numpy as np

class FaceRecognitionTrainer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.people_list = os.listdir(data_path)
        self.labels = []
        self.faces_data = []
        self.label = 0

    def train_model(self):
        for name_dir in self.people_list:
            person_path = os.path.join(self.data_path, name_dir)
            for file_name in os.listdir(person_path):
                print('Faces: ', name_dir + '/' + file_name)
                self.labels.append(self.label)
                face_image = cv2.imread(os.path.join(person_path, file_name), 0)
                self.faces_data.append(face_image)
            self.label += 1

        face_recognizer = cv2.face.EigenFaceRecognizer_create()
        face_recognizer.train(self.faces_data, np.array(self.labels))
        face_recognizer.write('modelEigenFace.xml')
