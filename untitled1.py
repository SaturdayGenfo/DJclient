# -*- coding: utf-8 -*-

from audiolib import autocorr
from severlib import send

import sounddevice as sd
import pyaudio
import time
import numpy as np

def mixerlist():
    items = sd.query_devices()
    names = []
    for e in items:
        names.append(e['name'])
    return names

class listener():
    def __init__(self,length, mixer):
        self.CHUNK = length*44100
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 30

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK,
                input_device_index=mixer)
        self.f = open("D.txt", 'w')
    
    def record(self):
        #print("* Enregistrement commence")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            nparr = np.fromstring(data, dtype=np.int16)
            t, bpm = int(round(time.time()*1000, 0)), autocorr(nparr, self.RATE, 32)
            self.f.write(str(t) + " ".join([str(round(b, 0)) for b in bpm]) + '\n')
    def end(self):
        
        self.stream.close()
        self.p.terminate()
        self.f.close()
        #print("* Termine")







