import sys
import numpy as np

import argparse
import torch
import cv2
import pyzed.sl as sl
import torch.backends.cudnn as cudnn

sys.path.insert(0, './yolov5')
from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh
from utils.torch_utils import select_device
from utils.augmentations import letterbox

from threading import Lock, Thread
from time import sleep

import ogl_viewer.viewer as gl
import cv_viewer.tracking_viewer as cv_viewer
import time

lock = Lock()
run_signal = False
exit_signal = False

viewer = gl.GLViewer()
viewer2 = gl.GLViewer()

print('Two windows opened')
time.sleep(10)

viewer.exit()
viewer2.exit()




