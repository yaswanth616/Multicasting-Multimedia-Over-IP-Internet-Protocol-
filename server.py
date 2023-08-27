import socket
import struct
import sys
import cv2, imutils, socket
import numpy as np
import time
import base64
import threading, wave, pyaudio, time
from multiprocessing import Process
from scipy.io import wavfile
import moviepy.editor as mp
import pygame
import threading
from threading import *
from mserver import *
from lserver import *
import mserver as ms
import lserver as ls

def livestream():
	ls.livstream()
def multistream():
	ms.mstream()


if __name__=='__main__':
	p1 = Process(target=livestream)
	p1.start()
	p2 = Process(target=multistream)
	p2.start()	
	
	

		