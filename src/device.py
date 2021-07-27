from enum import Enum

import abc
import cv2

import numpy as np


class DeviceType(Enum):
    WEBCAM: int = 1


class Device(metaclass=abc.ABCMeta):
    def __init__(self, deviceType):
        self.deviceType: DeviceType = deviceType

    @abc.abstractclassmethod
    def getFrame(self) -> np.ndarray:
        pass

    @abc.abstractclassmethod
    def release(self) -> None:
        pass


class WebCamDevice(Device):
    def __init__(self, deviceType):
        super().__init__(deviceType)
        self.cam = cv2.VideoCapture(0)

    def getFrame(self) -> np.ndarray:
        ret, frame = self.cam.read()
        return frame

    def release(self) -> None:
        self.cam.release()