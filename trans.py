#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os
# import sys
#
# import matplotlib
# if os.name == 'posix' and "DISPLAY" not in os.environ:
#     matplotlib.use("Agg")
# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
#
#
# import matplotlib.pyplot as plt
#
# from fer import FER
# from fer import Video
# VIDEO = "/Users/igracheva/Downloads/facial_emotion_recognition-0.3.4/sts/dna.mp4"
#
# if __name__ == "__main__":
#     try:
#         videofile = sys.argv[1]
#     except:
#         videofile = VIDEO
#     detector = FER(mtcnn=True)
#     video = Video(videofile)
#
#     # Output list of dictionaries
#     raw_data = video.analyze(detector, display=False)
#
#     # Convert to pandas for analysis
#     df = video.to_pandas(raw_data)
#     df = video.get_first_face(df)
#     df = video.get_emotions(df)
#
#     # Plot emotions
#     df.plot()
#     plt.show()