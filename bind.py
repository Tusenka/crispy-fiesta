import random

import cv2 as cv
import face_recognition as fs
from fer import FER
from pandas import datetime
from tinydb import TinyDB, Query

from codons import EMOTION_CODES
from emotional_storage import FacialFeatureStorage
from facial_reckognition import FacialReckognition
from guard_system import GuardSystem
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

VIDEO = f"{dir_path}/dna.mp4"
cam = cv.VideoCapture(VIDEO)


def pcr(dna):
    top_emotion = max(dna["emotions"], key=lambda key: dna["emotions"][key])
    return EMOTION_CODES[top_emotion.upper()], top_emotion
    pass


detector = FER(mtcnn=True,
               cascade_file="/Users/igracheva/Downloads/facial_emotion_recognition-0.3.4/greate_nano/mxnet_deploy_ssd_FP16_FUSED.xml",
               emotion_model="/Users/igracheva/Downloads/facial_emotion_recognition-0.3.4/sts/affectnet_emotions/mobilenet_7.h5")

storage = FacialFeatureStorage()
fr = FacialReckognition()
elf4 = GuardSystem(cv.VideoCapture(VIDEO), lambda s: print(str(s)))

while True:
    success, frame = cam.read()
    try:
        dna = detector.detect_emotions(frame)
        for gene in dna:
            print(gene)
            emotion, raw = pcr(gene)
            face, newFace = fr.reckognize_face(frame_=frame, facial_location=gene["box"])
            time_ = cam.get(cv.CAP_PROP_POS_MSEC)
            if newFace:
                elf4.invoke_alarm(time_=time_, img=frame, face=face)
            storage.store_state(time_=time_, face_id=face["id"], emotion=raw,
                                emotion_code=emotion)
            if random.randint(0,11)==9:
                storage.store_sample_img(img=frame,face_id=face['id'],time_=time_)
    except Exception as er:
        print("Unable to find a face or recognize an emotions\n e: {}".format(er))
        pass
