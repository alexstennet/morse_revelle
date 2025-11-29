import cv2
import numpy

class ImageProcess:

    def __init__(self):
        self.capture = cv2.VideoCapture('Video/Test_Video.mp4')
        if not self.capture.isOpened():
            print('Error: Could not open file')
            exit()
        self.frame_binary = []

    def ProcessVideo(self):
        """ Takes self.capture video file and goes frame by frame inputing it in a list of 1s and 0s corresponding with on and off
        """

        while True:
            ret, frame = self.capture.read()
            if not ret or frame is None:
                break

            if (frame.mean() > 150):
                self.frame_binary.append(1)
            else:
                self.frame_binary.append(0)

    def PrintFrameBinary(self):
        print(self.frame_binary)

class ConvertBinary:

    def __init__(self, frame_binary):
        self.frame_binary = frame_binary
        self.frame_morse = []
        self.unit = 1

    def BinaryToMorse(self):
        i = 0
        numSpace = 0
        while (i < len(self.frame_binary)):
            if (self.frame_binary[i] == 1):
                if (numSpace >= 7):
                    self.frame_morse.append(' ')

                if (self.frame_binary[i+self.unit] == 0):
                    self.frame_morse.append('.')
                elif(self.frame_binary[i+self.unit] == 1 and self.frame_binary[i+2*self.unit] == 1):
                    self.frame_morse.append('-')
            
            elif (self.frame_binary[i] == 0):
                numSpace += 1

            i += self.unit





            
            