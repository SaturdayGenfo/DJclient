# -*- coding: utf-8 -*-

from audiolib import autocorr
from severlib import send

import pyaudio
import time
import numpy as np


class listener():
    def __init__(self,length):
        
        
        self.CHUNK = length*44100
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 100

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK,
                input_device_index=12)

    
    def record(self):
        print("* Enregistrement commence")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            nparr = np.fromstring(data, dtype=np.int16)
            t, bpm = int(round(time.time()*1000, 0)), autocorr(nparr, self.RATE, 32)
            print(t, bpm)
    def end(self):
        print("* Termine")
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

a = listener(5)
a.record()
a.end()





