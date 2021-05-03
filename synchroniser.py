import random

import boto3
import cv2 as cv
import face_recognition as fs
from fer import FER
from pandas import datetime
from tinydb import TinyDB, Query

class Synch:

    def __init__(self, bucket, accessKey, secretKey):

        self.bucket = bucket
        self.secretKey = secretKey
        self.accessKey = accessKey
        self.next_step = boto3.resource("s3")

    def synchronise(self, folder, key):
        s3 = boto3.client('s3')
    #     TODO:


    def schedule_synchronise(self, folder, key):
        s3=boto3.resource("s3")
        
