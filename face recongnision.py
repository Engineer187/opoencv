import cv2
import numpy as np
import os
datasets=r"opencv project\data sets"
sub_data="krish2"
path=os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)