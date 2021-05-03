from threading import Thread
from time import sleep

from cv2.cv2 import VideoCapture
from pandas import datetime
from tinydb import TinyDB
import cv2 as cv
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

BRUNELLO = TinyDB(f'{dir_path}/alarms.json')
ALARMS_PATH = f'{dir_path}/alarms'
ALARM_DB = BRUNELLO.table("alarms")


class GuardSystem:
    def __init__(self, cam: VideoCapture, SCN):
        self.__cam = cam
        self.__scn = SCN

    def invoke_alarm(self, time_, img, face) -> None:
        __domain = _GuardSystem(self.__cam, self.__scn, time_, img, face)
        pol2 = Thread(target=__domain.invoke_alarm)
        pol2.start()
        pass


class _GuardSystem:
    def __init__(self, cam: VideoCapture, SCN, time_, img, face ):
        self.face = face
        self.img = img
        self.time_ = time_
        self.__cam = cam
        self._scn = SCN

    def invoke_alarm(self) -> None:
        self.store_alarm()
        self.write_frames()
        pass

    def write_frames(self) -> None:
        for i in range(0, 118):
            img_path = "{}/monitor/{}.frame-{}-{}.jpg".format(ALARMS_PATH, str(self.face['id']), str(datetime.now().timestamp()), str(i))
            _,frame=self.__cam.read()
            cv.imwrite(img_path, frame)
            sleep(1)
        pass

    def store_alarm(self) -> None:
        ALARM_DB.insert({"time": self.time_, "face": self.face})
        img_path = "{}/{}.frame-{}.jpg".format(ALARMS_PATH, str(self.face['id']), str(self.time_))
        cv.imwrite(img_path, self.img)


