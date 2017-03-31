# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:09:32 2017

@author: leello
"""
from scipy.fftpack import fft, ifft
from scipy.signal import decimate, fftconvolve
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# On se limite à des bpm compris entre 30 et 300.
# le découpage en bande de fréquence n'est utilisé que pour des fichiers musicaux. Pour des donnes accélérométriques, la bande de fréquence mise en jeu est peu large donc cette démarche n'est pas nécessaire.
# à partir des bornes d'une bande fréqence, de la fréquence d'échantillonnage, et du nombre de points prélevés, retourne la valeur normalisée des bornes de la bande.
def band(f1, f2, fe, N):
    p1 = 1.0*f1/fe * N
    p2 = 1.0*f2/fe *N
    return int(p1), int(p2)
def differentiate(env, n):
    N = env.shape[0]
    W = np.concatenate([np.ones(n), -1*np.ones(n)], 0)
    WEtendu = np.concatenate([W, np.zeros(N-2*n)], 0)
    derivee = ifft(np.multiply(fft(WEtendu), fft(env)))
    return derivee 
# A partir d'un signal et de sa fréquence d'échantillonnage, découpe le signal en 6 sous-signaux, chacun correspondant à une plage de fréquence différente. Pour cela on réalise une TF et on multiplie le signal par une porte de largeur choisie, puis on prend la TF inverse.
def chopUp(s, fe):
    N = s.shape[0]
    bandes = [(0,200), (200,400), (400,800), (800, 1600), (1600,3200), (3200, fe//2)]
    signaux = []
    for (f1, f2) in bandes :
        b1, b2 = band(f1, f2, fe, N)
        filt = []
        for i in range(N//2):
            if i >=b1 and i< b2:
                filt.append(1)
            else :
                filt.append(0)
        filt = np.concatenate([filt, filt[::-1]]) #On prend aussi les symétrique par rapport à N//2
        signaux.append(ifft(np.multiply(fft(s), filt)))
    return signaux
def energy(s):
    return np.sum(np.abs(np.multiply(s, s)))
def rectify(signal):
    return np.abs(signal)
    
# Retourne x+ du signal passé en paramètre
def halfRectify(signal):
    return np.array([max(s, 0) for s in signal])
def envelope(s, fe, dfact, show=True, k=1000):
    N = s.shape[0]
    s2 = rectify(s)  
    h = hhanning(fe)
    env = fftconvolve(s2, h)[len(h):-len(h)]
    denv = decimate(real(env), dfact, zero_phase=True)
    d = real(halfRectify(differentiate(denv, 50)))
    return d
    
# retourne la composante réelle du signal
def real(s):
    r = np.vectorize(lambda x : x.real)
    return r(s)
# filtre passe bas
def hhanning(fe):
    N = 0.1*fe
    X = np.arange(N//2, N)
    return 0.5*(1-np.cos(2.0*np.pi*X/N))
def autocorr(s, fe, dfact):
    l = chopUp(s, fe)
    l = l[:2] + l[4:]
    bpm = []
    for k in l:
        d = envelope(k, fe, dfact, False)
        bpm.append(determinate_bpm(d, fe//dfact, False))
    return bpm
    
def determinate_bpm(s,fe, show=True) :
    autocorr = signal.fftconvolve(s, s[::-1], mode='full')
    N=s.shape[0]
    m = np.argmax(autocorr[N + int(0.33*fe):N + int(1*fe)]) * (1.0/fe) + 0.33
    return  round(1.0/m * 60, 0)
