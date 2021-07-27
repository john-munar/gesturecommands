import cv2

import numpy as np

class Viewer:
    def __init__(self):
        self.frames: list = []

    def storeNextFrame(self, img: np.ndarray) -> None:
        self.frames.append(img)

    def display(self) -> None:
        if len(self.frames) != 0:
            cv2.imshow('Webcam', self.frames[0])
            self.frames.pop()

    def didKeyPressed(self, key: int) -> bool:
        return (True if cv2.waitKey(1) == key else False)

    def destroy(self) -> None:
        cv2.destroyAllWindows()