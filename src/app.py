from device import Device, WebCamDevice, DeviceType
from viewer import Viewer

import numpy as np

class App:
    def __init__(self):
        self.device: Device = WebCamDevice(DeviceType.WEBCAM)
        self.viewer: Viewer = Viewer()

    def run(self) -> None:
        while True:
            frame: np.ndarray = self.device.getFrame()
            self.viewer.storeNextFrame(frame)
            self.viewer.display()

            if self.viewer.didKeyPressed(key=ord('q')):
                break
        
        self.device.release();
        self.viewer.destroy()