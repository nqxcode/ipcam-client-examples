#!/usr/bin/env python3

import cv2
from pprint import pprint

#print("Before URL")
cap = cv2.VideoCapture('rtsp://10.0.250.10:554/user=admin&password=&channel=1&stream=1.sdp?real_stream')
#print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Inside",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
