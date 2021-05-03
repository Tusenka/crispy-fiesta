import random

import cv2 as cv
import face_recognition as fs
from fer import FER
from pandas import datetime
from tinydb import TinyDB, Query
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
BRUNELLO = TinyDB(f'{dir_path}/face.json')
FACE_DB = BRUNELLO.table("amazing_faces")
FACE_MAPPING_DB = BRUNELLO.table("amazing_faces_mapping")
ATTEND_DB = BRUNELLO.table("amazing_faces_mapping")
EMOTION_DB = BRUNELLO.table("amazing_emotion")
STATE_PATH = f'{dir_path}/samples/monitor'


class FacialFeatureStorage:

    def store_state(self, time_, face_id, emotion, emotion_code) -> None:
        EMOTION_DB.insert({'time': time_, 'face_id': face_id, "emotion": emotion, "emotion_code": emotion_code})
        # self.log(time_, [str(emotion), face_id, emotion])

    def store_sample_img(self, img, face_id, time_) -> None:
        img_path = "{}/{}.frame-{}.jpg".format(STATE_PATH, str(face_id), str(time_))
        cv.imwrite(img_path, img)

    def log(self, ar_timestamp, values):
        try:
            ar_timestamp = int(round(ar_timestamp))
            with open('ras.csv', 'a') as f:
                print("{};{}".format(ar_timestamp, ";".join(values)), file=f)
        except Exception as e:
            print("Unable to push to cloudwatch\n e: {}".format(e))
            return True

