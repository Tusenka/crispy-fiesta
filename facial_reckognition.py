import random

import cv2 as cv
import face_recognition as fs
from fer import FER
from pandas import datetime
from tinydb import TinyDB, Query
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
BRUNELLO = TinyDB(f'{dir_path}/face.json')
SAMPLES_PATH = f'{dir_path}/samples'
FACE_DB = BRUNELLO.table("amazing_faces")


class FacialReckognition:

    def reckognize_face(self, frame_, facial_location):
        encoding = fs.face_encodings(frame_, [facial_location])[0]
        FaceQuery = Query()
        faces = FACE_DB.search(FaceQuery.encodings.test(lambda encodings: fs.compare_faces(encodings, encoding)))
        if len(faces):
            face = faces[0]
            return face, False
        else:
            face_id = random.randint(0, 111825)
            time = datetime.now()
            img_path = "{}/{}.frame-{}.jpg".format(SAMPLES_PATH, face_id, time)
            face = {"id": face_id, "encodings": [encoding.tolist()], "sample": img_path, "name": "yourknowmyname",
                    "trusted": False}
            FACE_DB.insert(face)
            cv.imwrite(img_path, frame_)
            return face, True
