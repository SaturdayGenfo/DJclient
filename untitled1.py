# -*- coding: utf-8 -*-

from audiolib import autocorr


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
        self.RECORD_SECONDS = 300

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK,
                input_device_index=mixer)
        
    
    def record(self):
        #print("* Enregistrement commence")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            nparr = np.fromstring(data, dtype=np.int16)
            t, bpm = int(round(time.time()*1000, 0)), autocorr(nparr, self.RATE, 32)
            self.f = open("D.txt", 'a')
            self.f.write(str(int(round(time.time(), 0)) % 100000) + " ".join([str(round(b, 0)) for b in bpm]) + '\n')
            self.f.close()
    def end(self):
        
        self.stream.close()
        self.p.terminate()
        
        #print("* Termine")







